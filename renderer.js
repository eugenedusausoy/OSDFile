document.getElementById('tidyBtn').addEventListener('click', () => {
    // Eventually, request to Python backend here
    console.log('Tidy Folder button clicked');

    // For now, trigger the Python script through main process
    window.api.runPythonScript();
});
