// ============================================================
// ELEMENTS
// ============================================================

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");


const predictButton =
    document.getElementById(
        "predictBtn"
    );


const clearButton =
    document.getElementById(
        "clearBtn"
    );


const uploadInput =
    document.getElementById(
        "imageInput"
    );


const uploadPredictButton =
    document.getElementById(
        "uploadPredictBtn"
    );


const preview =
    document.getElementById(
        "preview"
    );


const digitElement =
    document.getElementById(
        "digit"
    );


const confidenceElement =
    document.getElementById(
        "confidence"
    );


const probabilitiesElement =
    document.getElementById(
        "probabilities"
    );


// ============================================================
// CANVAS
// ============================================================

let drawing = false;


function clearCanvas() {

    ctx.fillStyle = "black";

    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    digitElement.textContent = "?";

    confidenceElement.textContent =
        "Upload or draw a digit";

    probabilitiesElement.innerHTML = "";
}


clearCanvas();


// ============================================================
// GET POSITION
// ============================================================

function getPosition(event) {

    const rect =
        canvas.getBoundingClientRect();


    const source =
        event.touches
            ? event.touches[0]
            : event;


    return {

        x:
            (source.clientX - rect.left)
            *
            (canvas.width / rect.width),

        y:
            (source.clientY - rect.top)
            *
            (canvas.height / rect.height)

    };
}


// ============================================================
// START DRAWING
// ============================================================

function startDrawing(event) {

    drawing = true;

    event.preventDefault();


    const position =
        getPosition(event);


    ctx.beginPath();


    ctx.moveTo(
        position.x,
        position.y
    );
}


// ============================================================
// DRAW
// ============================================================

function draw(event) {

    if (!drawing) {
        return;
    }


    event.preventDefault();


    const position =
        getPosition(event);


    ctx.lineWidth = 18;

    ctx.lineCap = "round";

    ctx.lineJoin = "round";

    ctx.strokeStyle = "white";


    ctx.lineTo(
        position.x,
        position.y
    );


    ctx.stroke();
}


// ============================================================
// STOP DRAWING
// ============================================================

function stopDrawing(event) {

    if (!drawing) {
        return;
    }


    event.preventDefault();


    drawing = false;

    ctx.closePath();
}


// ============================================================
// MOUSE
// ============================================================

canvas.addEventListener(
    "mousedown",
    startDrawing
);


canvas.addEventListener(
    "mousemove",
    draw
);


canvas.addEventListener(
    "mouseup",
    stopDrawing
);


canvas.addEventListener(
    "mouseleave",
    stopDrawing
);


// ============================================================
// TOUCH
// ============================================================

canvas.addEventListener(
    "touchstart",
    startDrawing,
    { passive: false }
);


canvas.addEventListener(
    "touchmove",
    draw,
    { passive: false }
);


canvas.addEventListener(
    "touchend",
    stopDrawing,
    { passive: false }
);


// ============================================================
// CLEAR
// ============================================================

clearButton.addEventListener(
    "click",
    clearCanvas
);


// ============================================================
// SHOW RESULT
// ============================================================

function showResult(result) {

    digitElement.textContent =
        result.digit;


    confidenceElement.textContent =
        "Confidence: "
        +
        result.confidence
        +
        "%";


    probabilitiesElement.innerHTML = "";


    result.probabilities.forEach(
        function(probability, index) {

            const row =
                document.createElement(
                    "div"
                );


            row.className =
                "probability-row";


            row.innerHTML = `

                <span class="label">
                    ${index}
                </span>

                <div class="bar-container">

                    <div
                        class="bar"
                        style="width:${probability}%"
                    ></div>

                </div>

                <span class="value">
                    ${probability}%
                </span>

            `;


            probabilitiesElement
                .appendChild(row);

        }
    );
}


// ============================================================
// DRAWING PREDICTION
// ============================================================

predictButton.addEventListener(
    "click",
    async function() {

        digitElement.textContent = "...";

        confidenceElement.textContent =
            "CNN is predicting...";


        try {

            const imageData =
                canvas.toDataURL(
                    "image/png"
                );


            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify({
                                image:
                                    imageData
                            })

                    }
                );


            const result =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    result.error
                );

            }


            showResult(result);


        }
        catch (error) {

            digitElement.textContent =
                "!";


            confidenceElement.textContent =
                error.message;

        }

    }
);


// ============================================================
// IMAGE UPLOAD PREVIEW
// ============================================================

uploadInput.addEventListener(
    "change",
    function() {

        const file =
            uploadInput.files[0];


        if (!file) {

            preview.style.display =
                "none";

            return;
        }


        const imageURL =
            URL.createObjectURL(file);


        preview.src =
            imageURL;


        preview.style.display =
            "block";

    }
);


// ============================================================
// UPLOADED IMAGE PREDICTION
// ============================================================

uploadPredictButton.addEventListener(
    "click",
    async function() {

        const file =
            uploadInput.files[0];


        if (!file) {

            alert(
                "Please select an image first."
            );

            return;
        }


        digitElement.textContent =
            "...";


        confidenceElement.textContent =
            "Processing uploaded image...";


        probabilitiesElement.innerHTML =
            "";


        try {

            // Create FormData
            const formData =
                new FormData();


            formData.append(
                "file",
                file
            );


            // Send image to Flask
            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        body: formData

                    }
                );


            const result =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    result.error
                );

            }


            showResult(result);


        }
        catch (error) {

            digitElement.textContent =
                "!";


            confidenceElement.textContent =
                error.message;

        }

    }
);