---
name: living-image-roi
description: Measure and record fluorescence or bioluminescence ROIs in the Windows Living Image (IVIS) desktop app, including in vivo tumor and ex vivo organ workflows, Excel recording, and optional GraphPad Prism XY export. 用于 Living Image 活体肿瘤或离体脏器 ROI 定量、Excel 汇总和 Prism 宽表整理。
---

# Living Image ROI measurements

Use the desktop control tool available in the current client. Follow its rules for permissions, capture, verified window targeting, and batching. The same skill works with either client's tool names. For on-screen controls and recovery, see [Living Image and Excel notes](references/desktop-workflow.md). For organ panels, read [Ex vivo organ ROIs](references/organ-roi.md).

## Identify the measurement

- Use the dataset, exposure, metric, ROI method, and save instructions already specified in the conversation. Ask only when a missing choice can change the measurement or where it is recorded.
- For a new in vivo fluorescence workflow with no settings specified, use the first fluorescence image, Binning 2, Smoothing None, circular Auto 1 at 50%, and **Avg Radiant Efficiency**. State the settings used. For bioluminescence, use the requested **Avg Radiance** or **Total Flux**. Record the metric and its units verbatim.
- Use the study's naming convention. For group labels like `Demo-A-24H-1-3`, the trailing fields represent time and the inclusive mouse range; the group itself may contain hyphens. In studies where the Browser's Group label encodes the intended time, use it and flag disagreement with the Time Point column. Confirm mouse order and identity when the layout or labels are ambiguous.

## In vivo tumor sequence

1. In the Living Image Browser, expand the target SEQ and open the agreed IMG. Verify its image ID and the number and arrangement of animals.
2. If the image already has the requested ROIs, check their order and contours and read the existing measurements. For new ROIs, apply the agreed Binning and Smoothing via **Tool Palette → Corrections / Filtering**.
3. Under **ROI Tools**, select **Auto 1** from the circular ROI menu. Use the agreed threshold. The crosshair may start on any animal. Drag it onto the tumor peak for the first animal in the agreed order and click **Create**. Move the crosshair and repeat for the other mice, then click **Done**.
4. Check every contour against the tumor position. Ask for the target location if the fluorescence is diffuse or several competing peaks make the tumor unclear. Compare ROI labels against mouse identity, especially if a dataset already had ROIs.
5. Open **Measure ROIs** once per image and confirm the Image Number and target column. Overlay labels may display a **total** while the results table also contains an **average**. Use the requested column.
6. Preserve the source dataset for review unless the user requests saving the ROI changes. If saving, verify the image ID before committing the dataset.

## Excel output

Use a long table with one row per animal for in vivo data. Include **Group**, **Time (h)**, **Mouse No.**, the measured metric and units, and **Image Number**. Keep the destination's existing time format if one exists. Organ panels use one row per mouse and organ.

Verify the workbook, sheet, and next empty row. Append the batch as numeric values using the available Excel integration or desktop input method. Check the written values and IDs against the measurement table, using scientific notation for display when helpful. Save according to the user's instructions.

## Optional Prism XY export

For in vivo long tables, run [wide_table.py](scripts/wide_table.py) with Python 3 and `openpyxl`. Use a saved workbook copy, with the first four columns ordered Group, Time (h), Mouse No., and numeric ROI value. The script accepts numeric hours or strings like `24H`, keeps absent observations blank, and rejects duplicate group/time/mouse records.

```sh
python scripts/wide_table.py build results.xlsx prism.tsv
python scripts/wide_table.py check results.xlsx --wide-sheet 1
```

Run these commands from the skill folder. Paste the generated TSV into a new Excel worksheet at A1 before running the check on the saved workbook. Confirm that mouse IDs refer to the same individuals across time points when a Prism analysis treats the columns as repeated measurements.
