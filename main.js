const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const path = require('path');

// Create the main window
function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 900,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'renderer.js'),  // For communication with UI
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile('index.html');  // Load the UI (index.html)
}

// Run the Python script for folder tidying
function runPythonScript() {
    const pythonProcess = exec('python3 backend/tidy.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing script: ${error}`);
            return;
        }
        console.log(`Python script output: ${stdout}`);
    });
}

// Electron's lifecycle methods
app.whenReady().then(() => {
    createWindow();

    // Call Python script when Electron app is ready (for testing)
    runPythonScript();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
