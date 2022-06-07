# FLOWCHART 流程图画法

`2021.04.20`
目前已知可以绘画流程图的方法。

## markdown flow chart

markdown 有 flowchart 等扩展 (mermaid 也可以画一点简单的示意图）
> [markdown 画图之一：流程图（flowchart）](https://blog.csdn.net/googgirl/article/details/108335574)
> [Flowchart.js 首页、文档和下载 - 流程图插件](https://www.oschina.net/p/flowchart-js?hmsr=aladdin1e1)

基本语句：`tag=>type: content:>url`

- `tag` 就是元素名字，
- `type` 是这个元素的类型，有 6 中类型，分别为：
    - 开始（椭圆形）：`start`
    - 结束（椭圆形）：`end`
    - 操作（矩形）：`operation`
    - 多输出操作（矩形）：`parallel`
    - 条件判断（菱形）：`condition`
    - 输入输出（平行四边形）：`inputoutput`
    - 预处理 / 子程序（圣旨形）：`subroutine`
- `content` 就是在框框中要写的内容，注意 type 后的冒号与文本之间一定要有个空格。
- `url` 是一个连接（网址），与框框中的文本相绑定

```flow chart
start=>start: start
operation1=>operation: operation1
isSuccess=>condition: success?
operation2=>operation: operation2
operation3=>operation: operation3
operation4=>operation: operation4
end=>end: 结束

start->operation1->isSuccess
isSuccess(yes)->operation2->end
isSuccess(no,left)->operation3->operation4(left)->operation1
```

```flow_chart_code
\\flow chart
\\第一部分声明结点
start=>start: start
operation1=>operation: operation1
isSuccess=>condition: success?
operation2=>operation: operation2
operation3=>operation: operation3
operation4=>operation: operation4
end=>end: 结束

\\第二部分链接节点
start->operation1->isSuccess
isSuccess(yes)->operation2->end
isSuccess(no,left)->operation3->operation4(left)->operation1
```

关键字

- `yes/true`：condition 类型变量连接时，用于分别表示 yes 条件的流向
- `no/false`：同上，表示否定条件的流向
- `left/right`：表示连线出口在节点位置（默认下面是出口，如 op3），可以跟 condition 变量一起用：cond (yes,right)
- `path1/path2/path3`：parallel 变量的三个出口路径（默认下面是出口）

节点状态
为节点设置不同的状态，可以通过不同的颜色显示，其中状态包括下面 6 个，含义如英文所示，

- past
- current
- future
- approved
- rejected
- invalid

```flow
st=>start: Start
e=>end: 需求变更备案
op1=>operation: 需求基线确定|past
op2=>operation: 内部需求变更|current
op3=>operation: 下一个版本|current
op4=>operation: 与客户协商需求变更|current
op5=>operation: 更新需求文档|current
op6=>operation: 通知项目组开发和测试|current
op7=>operation: 客户需求变更流程|current

cond1=>condition: 是否对实际业务产生影响
cond2=>condition: 是否接受当前版本变更

st->op1(right)->op1(right)->op2->cond1
cond1(no)->cond2
cond1(yes)->op4->op7
cond2(yes)->op5
cond2(no)->op3
op5->op6
op6->e
```

- 优点：只需要写出结点关系，连接关系，就自动排版
- 缺点：观赏性中等，自定义程度没有. 特别复杂的画不了，会有穿线的情况.

## 在线流程图制作

drawio 可以在线画很多厉害的图形，与 Visio 相比可能不那么专业一些但门槛更低一些.

不过流程图的图形感觉一般，需要手动调整
最致命的是，流程图中循环部分会出现线条绕回去并到之前的线条的情况，而 drawio 画不出来（箭头只能连到图形上，不能连到线条上）
有有限的数学公式支持，`$$公式$$`但是公式会另起一行.

## Visio

理论上可定制化程度较高，但**无法插入数学公式**，并且图形需要手动调整.

## latex

完全通过代码画图

- 优点
    - 非常严谨，可以统一规定字体大小，箭头形状等
    - 程序有一定自动处理的能力，比如方框会随着字数调整大小
    - 连线语法也比较方便
    - 支持行内公式等各种公式，只要 latex 支持的都可以
    - 美观度较高
- 缺点
    - 总体语法复杂，入门门槛高
    - latex 本身是不自带画流程图功能的，使用的 tikz 包也并没有专用的工具，需要自己花时间进行预设（好在可以调一个模板一直用）.
    - 画的过程也有麻烦的地方，比如线条要拐弯，就需要定义一下拐弯处的点，先连到点处，再连到另一个地方.

具体教程大概会总结到 Latex 使用里面吧.
