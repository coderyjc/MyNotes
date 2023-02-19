## 标签词云

```dataviewjs
const datas=dv.pages().flatMap(p => p.file.etags).groupBy(p => p).map(p => ({name: p.key.replace("#",""), value: p.rows.length})).array();
datas.forEach((data)=>{
	data['search']='tag'
})
 console.log(datas)
var option = {
	tooltip: {},
    series: [{
        type: 'wordCloud',

        // The shape of the "cloud" to draw. Can be any polar equation represented as a
        // callback function, or a keyword present. Available presents are circle (default),
        // cardioid (apple or heart shape curve, the most known polar equation), diamond (
        // alias of square), triangle-forward, triangle, (alias of triangle-upright, pentagon, and star.

        shape: 'pentagon',

        // Keep aspect ratio of maskImage or 1:1 for shapes
        // This option is supported from echarts-wordcloud@2.1.0
        keepAspect: false,

        // A silhouette image which the white area will be excluded from drawing texts.
        // The shape option will continue to apply as the shape of the cloud to grow.

		
        // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
        // Default to be put in the center and has 75% x 80% size.
        width: '100%',
        height: '100%',
        right: null,
        top: '-10%',
        // Text size range which the value in data will be mapped to.
        // Default to have minimum 12px and maximum 60px size.

        sizeRange: [20, 80],

        // Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90] by rotationStep 45

        rotationRange: [-30, -30],
        rotationStep: 45,

        // size of the grid in pixels for marking the availability of the canvas
        // the larger the grid size, the bigger the gap between words.

        gridSize: 8,

        // set to true to allow word being draw partly outside of the canvas.
        // Allow word bigger than the size of the canvas to be drawn
        drawOutOfBound: false,

        // If perform layout animation.
        // NOTE disable it will lead to UI blocking when there is lots of words.
        layoutAnimation: true,

        // Global text style
        textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            // Color can be a callback function or a color string
            color: function () {
                // Random color
                return 'rgba(' + [
                Math.round(Math.random() * 128) + 64,
                Math.round(Math.random() * 150),
                 Math.round(Math.random() * 128) + 50,
                 0.7
                            ].join(',') + ')';
            }
        },
        emphasis: {
            textStyle: {
                textShadowBlur: 2,
                color: '#528'
            }
        },

        // Data is an array. Each array item must have name and value property.
        data: datas
    }]
}
app.plugins.plugins['obsidian-echarts'].render(option, this.container)
```

## 按文件夹分组标签

```dataviewjs
// 基于文件夹聚类所有的标签。
for (let group of dv.pages("").filter(p => p.file.folder != "").groupBy(p => p.file.folder.split("/")[0])) {
  let datas=dv.pages(`"${group.key}"`).file.tags.distinct().map(t => {return `[${t}](${t})`}).array()
  let lens=datas.length
dv.paragraph(`## ${group.key} (${lens})`);

  dv.paragraph(
    datas.sort().join(" | "));
}

```


## 按标签分组

```dataview
TABLE WITHOUT ID (tag + "(" + length(rows.file.link) + ")") 
AS Tags, link(sort(rows.file.name)) 
AS Files 
FROM "" 
WHERE file.tags 
FLATTEN file.tags 
AS tag 
GROUP BY tag 
SORT file.name Asc 
```


