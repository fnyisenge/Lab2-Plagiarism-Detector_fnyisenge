#!/bin/bash
# setup.sh - initialize environment and record setup details

{
    echo "---- Setup started on the $(date) ----"

    # Create directories
    mkdir -p essays
    mkdir -p reports

    echo "Directories were created successfully: essays, reports"
    echo "Setup complete!"
    echo "---- End of log ----"
} >> setup.log

# Final confirmation message
echo "Setup successfully completed!"

