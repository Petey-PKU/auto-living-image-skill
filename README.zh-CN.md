# Auto Living Image Skill

[English](README.md) · 简体中文

这是 **Codex** 和 **Claude Code** 共用的技能，用于在 Living Image（IVIS）桌面软件中测量 ROI 并把结果汇总到 Excel。支持活体肿瘤和离体脏器 ROI，也可选导出 GraphPad Prism XY 宽表。桌面流程在 Windows 的 Living Image 4.3.1 上做过操作验证。

## 安装

下载或克隆仓库，将整个 [living-image-roi](living-image-roi/) 文件夹复制到对应客户端的技能目录。

| 客户端 | 用户技能目录 | 调用方式 |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/` | `$living-image-roi` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `/living-image-roi` |

打开 Living Image 的数据列表和目标 Excel 工作簿。当前会话需要可以访问这两个应用的桌面控制工具。只有使用可选的 Prism 导出时才需要 Python 3 和 `openpyxl`。

## 快速开始

> 测量 Demo A 组 24 h 的 1–3 号小鼠肿瘤 ROI。选第一张荧光图，Binning 设为 2，不平滑，按从左到右用 50% 阈值的圆形 Auto 1 圈选。把 Avg Radiant Efficiency 和图像编号追加到已打开的 Excel，保留图像供复核。

1. **打开图像。** 在 Living Image Browser 中展开匹配的序列，打开约定的那一张图。
2. **测量 ROI。** 在 **Tool Palette → ROI Tools** 中打开圆形 ROI 菜单，选择 **Auto 1**。核对各 ROI 的轮廓后打开 **Measure ROIs**。

   ![Living Image 的 ROI Tools 面板，已展开圆形 ROI 菜单并显示 Auto 1](docs/images/living-image-auto-1.png)

3. **记录结果。** 每只鼠在 Excel 中追加一行，记录测量指标、单位和来源图像编号。下图使用合成示例数值。

   ![Excel 长表中的三条合成 ROI 测量记录](docs/images/excel-roi-example.png)

## 导出到 Prism

在仓库根目录运行下列命令，用已保存的活体结果工作簿副本生成 TSV。宽表每行是一个时间点，每组小鼠的重复数据按列排列。把 TSV 粘贴到新工作表的 A1，保存后运行校验。工作表序号从 0 开始。

```sh
python -m pip install openpyxl
python living-image-roi/scripts/wide_table.py build results.xlsx prism.tsv
python living-image-roi/scripts/wide_table.py check results.xlsx --wide-sheet 1
```

## 开源协议

本项目的技能、脚本和文档采用 [GNU General Public License v3.0](LICENSE)。Living Image、Excel 和 GraphPad Prism 是各自独立的软件产品。
