# L3 标准版白天配图库

仓库：https://github.com/nikoyam303-alt/htx-creativeos/tree/main/assets/illustrations/l3-standard-light
索引：https://raw.githubusercontent.com/nikoyam303-alt/htx-creativeos/main/assets/illustrations/l3-standard-light/manifest.json

## 自动调用

从已安装 skill 所在目录运行（路径含空格时加引号）：

```sh
python3 scripts/l3_assets.py --query "交易赛 奖励" --limit 8
python3 scripts/l3_assets.py --id l3-light-7494-5755 --output /绝对路径/工作目录/illustration.png
```

1. 读取最新 manifest，按文案语义搜索名称、description、keywords。无命中时读取完整索引或换用同义词，不直接选择第一张。
2. 阅读 `contactSheets` 提供的总览（路径相对仓库根目录），或下载 2–3 个候选查看。名称相同不表示图案相同；以实际图意和版式空间决定。
3. 用明确 ID 下载所选透明 PNG，脚本核对 SHA-256；保留本次 ID 和 figmaNodeId 作为来源记录。
4. 等比排版，主体的浅色细节须在背景上清晰可见。检查最终图片的真实像素，不拉伸、裁切或修改原配图。

## 字段

每项含唯一 ID、Figma 原始名称、视觉描述、主题关键词、light 主题、L3标准版级别、仓库路径、1024×1024 像素、4× 导出倍率、透明标记、SHA-256 和 Figma 来源节点。临时 Figma 下载地址不入库。

## 缓存和失败处理

- 脚本支持 `--manifest 本地索引.json` 离线搜索；下载文件已存在且校验通过时直接复用。
- 索引请求失败：使用最近已校验的本地索引及素材，并说明缓存版本；不要伪称刚刚同步成功。
- 校验失败：重新取最新索引后重试一次，仍失败则报告具体素材 ID，不使用损坏或不匹配文件。
- 需要更新素材或更高分辨率时才使用 Figma MCP 的 renchao 账户。来源文件 `SzTzif4U7HRd2CorAGocTk`、页面 `7174:7829`；`9787:19522` 仅是分区标题，不是素材容器。
