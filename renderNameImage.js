function renderNameToImage(name, options = {}) {
    // Default options
    const {
        font = '40px Arial',
        color = 'black',
        backgroundColor = 'white',
        width = 400,
        height = 200,
        textAlign = 'center',
        textBaseline = 'middle',
        downloadFileName = 'name_image.png'
    } = options;

    // Create a canvas element
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const ctx = canvas.getContext('2d');

    // Fill background
    ctx.fillStyle = backgroundColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Set text styles
    ctx.font = font;
    ctx.fillStyle = color;
    ctx.textAlign = textAlign;
    ctx.textBaseline = textBaseline;

    // Draw the name on the canvas
    ctx.fillText(name, canvas.width / 2, canvas.height / 2);

    // Convert the canvas to an image
    const dataURL = canvas.toDataURL('image/png');

    // Create a download link
    const downloadLink = document.createElement('a');
    downloadLink.href = dataURL;
    downloadLink.download = downloadFileName;
    downloadLink.textContent = 'Download Image';
    document.body.appendChild(downloadLink);

    // Trigger the download
    downloadLink.click();

    // Clean up
    document.body.removeChild(downloadLink);
}

// Attach the function to the window object for global access
window.renderNameToImage = renderNameToImage;
