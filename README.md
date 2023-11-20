# PErfect Circle  

## Overview

This Python script utilizes the `pyautogui` library to draw a circle with 99% accuracy on the website [neal.fun](https://neal.fun/perfect-circle/). The circle is drawn by programmatically moving the mouse cursor around a specified radius in a circular motion.

## Requirements

- Python 3.x
- `pyautogui` library

## Instructions

1. Make sure you have Python 3.x installed on your system.
2. Install the `pyautogui` library by running the following command in your terminal:

    ```bash
    pip install pyautogui
    ```

3. Run the script using the following command:

    ```bash
    python circle_drawer.py
    ```

4. Place your cursor on the [neal.fun](https://neal.fun/perfect-circle/) website while in fullscreen mode.

5. The script will start drawing a circle with a specified radius. To stop the process, press before the countdown is over`Ctrl+C`.

## Parameters

- `Radius`: Adjust the value of the `Radius` variable to control the size of the circle. If the cursor moves out of the screen, try reducing the radius.

## Notes

- The script sets the cursor to the center of the screen before starting the circle drawing process.
- The process begins after a countdown from 5 to 0, allowing you to prepare.
- If you want to customize the circle further, you can modify the script accordingly.

## Caution

- Make sure the website is in fullscreen mode before running the script to ensure accurate drawing.

## Acknowledgments

This script is a fun and creative way to interact with the [neal.fun](https://neal.fun/perfect-circle/) website. It serves as a demonstration of how automation tools like `pyautogui` can be used for unconventional tasks.