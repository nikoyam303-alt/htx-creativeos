# 火宝配图库

来源：[Figma 火宝角色合集](https://www.figma.com/design/65lorIZe3ZfsWhJEJUZq0S?node-id=7389-2)。
仓库：[完整原图与预览](https://github.com/nikoyam303-alt/htx-creativeos/tree/main/assets/illustrations/htx-huobao)。

先检索动作/道具/用途，再看候选图；同名不同编号保留，不按名称去重。`sourceImageHash` 是 Figma 原图 SHA-1，`sha256` 用于下载完整性校验。

```sh
python3 scripts/huobao_assets.py --query "手机 OTC 出金"
python3 scripts/huobao_assets.py --id HB-274 --output work/huobao.png
python3 scripts/huobao_assets.py --manifest references/huobao-manifest.json --query "庆祝"
```

离线索引只能检索；下载仍需网络或已校验的目标文件。若没有准确匹配，不把相近动作说成完全符合。优先用原图构图适配；新增动作采用用户指定工具，并附官方参考图。
