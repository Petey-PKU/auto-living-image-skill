# Living Image and Excel notes

The UI labels below were observed in Living Image 4.3.1 on Windows. Locate controls in the current window after a layout, focus, or menu change. Use live controls or fresh observations for coordinates.

## Living Image

- The Browser **Load** button on a SEQ opens the sequence view. Expand it and select the IMG row to load a particular exposure, or double-click the IMG row.
- If **Tool Palette** is checked under **View** and you cannot see it, enlarge the main window to bring floating panels into view. Move the palette next to the image if it is parked at a screen edge.
- **Binning** and **Smoothing** are under **Corrections / Filtering**. An asterisk by a binning option indicates the original acquisition binning. Verify the selected value on each image that needs a new ROI.
- For circular Auto 1, use the arrow beside the circle icon under **ROI Tools**. Drag the crosshair to reposition it. The **Create** and **Done** buttons move with the crosshair.
- **Measure ROIs** is available in ROI Tools and under **View → ROI Measurements**. Check the Image Number, the ROI identifier, and the correct value column before recording.
- The screenshot batching available in each desktop runtime differs. Where permitted, plan several ROI centers from one stable view, follow the tool's required refresh steps, and read the measurement table once for the whole image.

## Excel

- An active Excel workbook may be different from the workbook you intend to update. Verify its title, sheet, and the destination range before writing.
- If the desktop tool supports pasting TSV as cells, paste the batch in one operation. A connected Excel tool can also write the full range. When working in a GUI, verify the first target cell in the Name Box and check that the pasted data spans the expected rows and columns.
- In a recent Excel desktop version, an array constant can populate a small range in one entry. Confirm the spill region is empty, then select it, copy it, and use **Paste Special → Values** to leave independent cells.
- Store measurement values as numbers and use scientific notation as a display format. After writing, compare the image IDs and the first and last rows against the source. For small batches, verify every row.
