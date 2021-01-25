# Ajax

ajax:Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

- Asynchronous: 异步的意思

- JavaScript：javascript脚本，在浏览器中执行

- and : 和

- xml : 是一种数据格式

ajax是一种做局部刷新的新方法（2003左右），不是一种语言。 ajax包含的技术主要有javascript, dom,css, xml等等。 核心是javascript 和 xml （json）。

javascript：负责创建异步对象， 发送请求， 更新页面的dom对象。 ajax请求需要服务器端的数据。

xml，现在是json

## 全局刷新和局部刷新

全局刷新： 整个浏览器被新的数据覆盖。 在网络中传输大量的数据。 浏览器需要加载，渲染页面。

局部刷新： 在浏览器器的内部，发起请求，获取数据，改变页面中的部分内容。 其余的页面无需加载和渲染。 网络中数据传输量少， 给用户的感受好。



 ajax是用来做局部刷新的。局部刷新使用的核心对象是 异步对象（XMLHttpRequest）， 这个异步对象是存在浏览器内存中的 ，使用javascript语法创建和使用XMLHttpRequest对象。

## 异步请求对象

步骤：

1. 创建异步对象 var xmlHttp = new XMLHttpRequest();

2. 给异步对象绑定事件。onreadystatechange ：当异步对象发起请求，获取了数据都会触发这个事件。这个事件需要指定一个函数， 在函数中处理状态的变化。
```java
// 例如：
    xmlHttp.onreadystatechange= function(){
       处理请求的状态变化。
		 if(xmlHttp.readyState == 4 && xmlHttp.status== 200 ){
           //可以处理服务器端的数据，更新当前页面
			  var data = xmlHttp.responseText;
			  document.getElementById("name").value= data;
		 }
    }
```

3. 初始异步请求对象 : 异步的方法open(). `xmlHttp.open(请求方式get|post, "服务器端的访问地址", 同步|异步请求（默认是true，异步请求）)`例如：xmlHttp.open("get", "loginServlet?name=zs&pwd=123",true);

4. 使用异步对象发送请求     `xmlHttp.send()`

异步对象的属性 readyState 表示异步对象请求的状态变化

- 0：创建异步对象时， new XMLHttpRequest();
- 1: 初始异步请求对象， xmlHttp.open()
- 2：发送请求， xmlHttp.send()
- 3: 从服务器端获取了数据，此时3， 注意3是异步对象内部使用， 获取了原始的数据。
- 4：异步对象把接收的数据处理完成后。 此时开发人员在4的时候处理数据。在4的时候，开发人员做什么 ？  更新当前页面。

异步对象的status属性，表示网络请求的状况的，  200， 404， 500， 需要是当status==200时，表示网络请求是成功的。

获取服务器端返回的数据， 使用异步对象的属性 responseText . `例子：xmlHttp.responseText `

回调：当请求的状态变化时，异步对象会自动调用onreadystatechange事件对应的函数。

访问地址： 使用get方式传递参数`http://localhost:8080/course_myajax/bmiPrint?name=李四&w=82&h=1.8`

前端实现：

```html
  <head>
    <title>UpAndDown</title>
    <script type="text/javascript">

      function doAjax() {
        // 使用内存中的一部对象，代替浏览器发起请求，异步对象使用js创建和管理。
        // 1. 创建对象异步对象
        var xmlHttp = new XMLHttpRequest();
        // 2. 绑定事件
        xmlHttp.onreadystatechange = function () {
          //处理服务器返回的数据，更新当前的页面
          // 响应成功, 更新部分页面
          if(xmlHttp.readyState === 4 && xmlHttp.status === 200){
            document.getElementById("result").innerText = xmlHttp.responseText;
          }
        }
        // 3. 初始请求数据
        // 获取dom对象的value属性值
        var height = document.getElementById("height").value;
        var weight = document.getElementById("weight").value;
        var param = "weight="+weight+"&height="+height;

        alert(param);

        xmlHttp.open("get", "result?" + param, true);
        // 4. 发起请求
        xmlHttp.send();
      }

    </script>
  </head>
    <body>
        身高<input type="text" id="height" />
        体重<input type="text" id="weight"/>
        <input type="button"  value="submit" onclick="doAjax()"/>
        <br>
        <br>
        <div id="result">结果</div>
    </body>
```

后端实现：

```java
public class ResultServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        double height = Double.parseDouble(request.getParameter("height"));
        double weight = Double.parseDouble(request.getParameter("weight"));
        double result = weight / (height * height);
        //---------------------
        response.setContentType("text/html; charset=utf-8");
        PrintWriter pw = response.getWriter();
        pw.println("您的BMI指数为 ： " +result);
        pw.flush();
        pw.close();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}
```

---

全局刷新源代码：`Learning\JavaWeb\Ajax\BMI-整体刷新`

局部刷新源代码：`Learning\JavaWeb\Ajax\BMI-局部刷新`



## json的使用

ajax发起请求-------servlet（返回的一个json格式的字符串 { name:"河北", jiancheng:"冀","shenghui":"石家庄"}）

json分类：

1. json对象 ，JSONObject ,这种对象的格式   名称:值， 也可以看做是 key:value 格式。
2. json数组， JSONArray, 基本格式  [{ name:"河北", jiancheng:"冀","shenghui":"石家庄"} , { name:"山西", jiancheng:"晋","shenghui":"太原"} ]

为什么要使用json

1. json格式好理解
2. json格式数据在多种语言中，比较容易处理。 使用java， javascript读写json格式的数据比较容易。
3. json格式数据他占用的空间下，在网络中传输快， 用户的体验好。

处理json的工具库： gson（google）； fastjson（阿里），jackson， json-lib

在js中的，可以把json格式的字符串，转为json对象， json中的key，就是json对象的属性名。

添加处理json的jar包：

jackson-annotations-2.9.0.jar
jackson-core-2.9.0.jar
jackson-databind-2.9.0.jar

代码：

详细代码见:`Learning\JavaWeb\Ajax\使用json+ajax`

前端

```html
    <script type="text/javascript">

      function doAjax() {
        // 使用内存中的一部对象，代替浏览器发起请求，异步对象使用js创建和管理。
        // 1. 创建对象异步对象
        var xmlHttp = new XMLHttpRequest();
        // 2. 绑定事件
        xmlHttp.onreadystatechange = function () {
          //处理服务器返回的数据，更新当前的页面
          // 响应成功
          if(xmlHttp.readyState === 4 && xmlHttp.status === 200){
              // eval 是执行括号中的代码，把json转换为json对象
              var jsonobj = eval("(" + xmlHttp.responseText + ")");
              // 更新json对象
              document.getElementById("name").value = jsonobj.name;
              document.getElementById("jiancheng").value = jsonobj.jiancheng;
          }
        }
        // 3. 初始请求数据
        // 获取dom对象的value属性值
        var id = document.getElementById("id").value;
        xmlHttp.open("get", "result?id=" + id, true);
        // 4. 发起请求
        xmlHttp.send();
      }

    </script>
```


后端

```java
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String sql = "select id, name, jiancheng, shenghui from province where id = ?";
        Object[] params = {request.getParameter("id")};
        ResultSet rs = DBUtil.executeQuery(sql, params);

        Province province;
        // 设置初始值。保证无论如何都会返回一个json格式的数据
        String json = "{}";

        try {
            if(rs.next()){
                province = new Province(rs.getString("id"),
                        rs.getString("name"),
                        rs.getString("jiancheng"),
                        rs.getString("shenghui"));
                ObjectMapper objectMapper = new ObjectMapper();
                json = objectMapper.writeValueAsString(province);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        response.setContentType("application/json;charset=utf-8");
        PrintWriter pw = response.getWriter();
        pw.println(json);
        pw.flush();
        pw.close();
    }
```