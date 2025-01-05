#!/bin/bash

# Define the screenshot file path
SCREENSHOT_FILE="/tmp/screenshot.png"

# Take a screenshot of a selected area
screencapture -i $SCREENSHOT_FILE

# Check if the screenshot was taken
if [ -f "$SCREENSHOT_FILE" ]; then
    # Call the Python script to process the image
    python3 process_image.py $SCREENSHOT_FILE
else
    echo "Screenshot was not taken."
fi
