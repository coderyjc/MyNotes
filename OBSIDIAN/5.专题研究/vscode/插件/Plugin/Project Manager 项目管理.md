---
type: 功能增强
name: Project Manager 项目管理
ootb: 0
recommendation: 7
create_date: 2022-01-27
---

![[assets/Pasted image 20220127142607.png]]

# Project Manager 项目管理

https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager

## 特点

-   将任何文件夹或工作区另存为**项目**
-   自动检测**Git**、**Mercurial**或**SVN**存储库
-   **使用标签**组织您的项目
-   在同一窗口或新窗口中打开项目
-   识别 _已删除/重命名的_ 项目
-   标识当前项目的**状态栏**
-   专用**侧边栏**

## 使用

-   `Project Manager: Save Project`将当前文件夹/工作区另存为新项目
-   `Project Manager: Edit Project`手动编辑您的项目 ( `projects.json`)
-   `Project Manager: List Projects to Open`列出所有已保存/检测到的项目并选择一个
-   `Project Manager: List Projects to Open in New Window`列出所有已保存/检测到的项目并选择一个在新窗口中打开
-   `Project Manager: Filter Projects by Tag`按选定标签过滤收藏项目

为了更轻松地自定义项目列表，您可以`projects.json`直接在**Code**中编辑文件。只需执行`Project Manager: Edit Projects`并`projects.json`打开文件。就这么简单：

```json
[
    {
        "name": "Pascal MI",
        "rootPath": "c:\\PascalProjects\\pascal-menu-insight",
        "tags": [],
        "enabled": true
    },
    {
        "name": "Bookmarks",
        "rootPath": "$home\\Documents\\GitHub\\vscode-bookmarks",
        "tags": [
            "Personal",
            "VS Code"
        ],
        "enabled": true
    },
    {
        "name": "Numbered Bookmarks",
        "rootPath": "~\\Documents\\GitHub\\vscode-numbered-bookmarks",
        "tags": [
            "Personal",
            "VS Code"
        ],
        "enabled": false
    }
]
```

> 您可以在定义任何路径时使用`~`或。`$home`它将被您的 HOME 文件夹替换。

> 确保 JSON 文件格式正确。否则，Project Manager 将无法打开它，并且应该会出现这样的错误消息。在这种情况下，您应该使用`Open File`按钮来修复它。


## 配置

您可以选择项目的排序方式

-   `Saved`：保存项目的顺序
-   `Name`：为项目键入的名称
-   `Path`: 项目的完整路径
-   `Recent`: 最近使用的项目

```json
    "projectManager.sortList": "Name"
```

更多设置见官网。