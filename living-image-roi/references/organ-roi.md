# Ex vivo organ ROIs

Confirm the plate map for the current study. One supported layout has one mouse per row and organs arranged left to right as heart, liver, spleen, lung, kidney, tumor, and muscle. Open the agreed image and verify the row and organ positions. Set the overlay so the organ boundaries are visible.

## Irregular Auto 1

1. Identify organ centers in the current image. Use the **irregular ROI** menu under **ROI Tools** and select **Auto 1**.
2. Drag the crosshair onto the organ, click **Create**, set **Threshold %**, press Enter, and check the contour before clicking **Done**. The threshold field may be disabled before Create or after Done. Start a fresh Auto 1 operation for each organ.
3. Record the ROI identifier against the organ and mouse as you go. Recreated ROIs can reuse an earlier number, so check the physical position before assigning a measurement.
4. Open **Measure ROIs** after the image is complete. Write one row per mouse and organ with Group, Time (h), Mouse No., Organ, the metric and units, Threshold %, and Image Number.

## Starting thresholds

These are example starting settings from one imaging workflow. Check each contour and adapt to the study and image. If a signal is too weak for Auto 1, ask whether to use an agreed manual ROI or leave the measurement blank.

| Organ | Example threshold |
| --- | ---: |
| Heart | 25% |
| Liver | 10% |
| Spleen | 15% |
| Lung | 30% |
| Kidney | 10% |
| Tumor | 10% |
| Muscle | Manual review |
