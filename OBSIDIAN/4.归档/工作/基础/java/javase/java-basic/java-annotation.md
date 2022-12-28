## 注解

Annotation

注解Annotation是一种引用数据类型。编译之后也是生成xxx.class文件。

怎么自定义注解呢？ [修饰符列表] @interface 注解类型名{ }

注解使用时的语法格式是：@注解类型名

注解可以出现在类上、属性上、方法上、变量上等....注解还可以出现在注解类型上。默认情况下，注解可以出现在任意位置。

### 内置注解

#### Override

关于JDK lang包下的Override注解
源代码：public @interface Override {}

- 标识性注解，给编译器做参考的。编译器看到方法上有这个注解的时候，编译器会自动检查该方法是否重写了父类的方法。如果没有重写，报错。
- 这个注解只是在编译阶段起作用，和运行期无关！
- @Override这个注解只能注解方法。
- @Override这个注解是给编译器参考的，和运行阶段没有关系。

凡是java中的方法带有这个注解的，编译器都会进行编译检查，如果这个方法不是重写父类的方法，编译器报错。
Override 表示一个方法声明打算重写超类中的另一个方法声明。

#### Deprecated

作用：告诉其他程序员这个标记的元素已经过时了。

注释的程序元素，不鼓励程序员使用这样的元素，通常是因为它很危险或存在更好的选择。

### 元注解

什么是元注解？用来标注“注解类型”的“注解”，称为元注解。

常见的元注解有哪些？Target/Retention

关于Target注解：这是一个元注解，用来标注“注解类型”的“注解”这个Target注解用来标注“被标注的注解”可以出现在哪些位置上。

@Target(ElementType.METHOD)：表示“被标注的注解”只能出现在方法上。
@Target(value={CONSTRUCTOR, FIELD, LOCAL_VARIABLE, METHOD, PACKAGE, MODULE, PARAMETER, TYPE})
表示该注解可以出现在：构造方法上/字段上/局部变量上/方法上/类上...


关于Retention注解：这是一个元注解，用来标注“注解类型”的“注解”这个Retention注解用来标注“被标注的注解”最终保存在哪里。

@Retention(RetentionPolicy.SOURCE)：表示该注解只被保留在java源文件中。
@Retention(RetentionPolicy.CLASS)：表示该注解被保存在class文件中。
@Retention(RetentionPolicy.RUNTIME)：表示该注解被保存在class文件中，并且可以被反射机制所读取。

### 注解中的属性

```java
public @interface MyAnnotation {
    /**
     * 我们通常在注解当中可以定义属性，以下这个是MyAnnotation的name属性。
     * 看着像1个方法，但实际上我们称之为属性name。
     * @return
     */
    String name();
    String color();
    int age() default 25; //属性指定默认值
}

public class MyAnnotationTest {
    //报错的原因：如果一个注解当中有属性，那么必须给属性赋值。（除非该属性使用default指定了默认值。）
    //@MyAnnotation(属性名=属性值,属性名=属性值,属性名=属性值)
    //指定name属性的值就好了。
    @MyAnnotation(name = "zhangsan", color = "红色")
    public void doSome(){
    }
}
```

```java
/*
如果一个注解的属性的名字是value(其他名字不行)，并且只有一个属性的话，在使用的时候，该属性名可以省略。
 */
public class MyAnnotationTest {

    // 报错原因：没有指定属性的值。
    /*@MyAnnotation
    public void doSome(){
    }*/

    @MyAnnotation(value = "hehe")
    public void doSome(){
    }

    @MyAnnotation("haha")
    public void doOther(){
    }
}
```

```java


```

需求：
假设有这样一个注解，叫做：@Id

这个注解只能出现在类上面，当这个类上有这个注解的时候，要求这个类中必须有一个int类型的id属性。如果没有这个属性就报异常。如果有这个属性则正常执行！