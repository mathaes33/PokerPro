// overlay/main.js

const { app, BrowserWindow, globalShortcut } = require('electron');

let overlayWindow;

function createWindow() {
  overlayWindow = new BrowserWindow({
    width: 800,
    height: 600,
    transparent: true,
    frame: false,
    alwaysOnTop: true,
  });

  overlayWindow.loadURL('http://localhost:3000');
}

app.whenReady().then(() => {
  createWindow();

  globalShortcut.register('CommandOrControl+Shift+O', () => {
    if (overlayWindow.isVisible()) {
      overlayWindow.hide();
    } else {
      overlayWindow.show();
    }
  });
});

app.on('will-quit', () => {
  globalShortcut.unregisterAll();
});