# VSCODE

## vscode debug

[使用 vscode 调试你的 node 应用](https://segmentfault.com/a/1190000019181649)
[Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging)

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File (Integrated Terminal)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "--config",
                "configs/example.json"
            ]
        },
.....
```

## Jupyter Notebook

[Please share your feedback on the Python Data Science experience in VS Code Survey](https://www.surveymonkey.com/r/QCSVHLL)

<!-- TODO: 仔细研究研究可以成为生产力工具. -->

使用方式

- 可以使用 Jupyter Notebook 建立的文件导入 (Import Jupyter Notebook Dialog).
- Notebook Editor
- Python Interactive Window (#%%)`.py`文件中输入`#%%`可以新建一个代码块，即 interactive mode
