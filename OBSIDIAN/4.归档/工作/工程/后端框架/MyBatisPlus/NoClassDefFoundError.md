### NoClassDefFoundError: org/apache/velocity/context/Context

缺少maven依赖

```xml
		<!-- 模板引擎 -->
		<dependency>
			<groupId>org.apache.velocity</groupId>
			<artifactId>velocity-engine-core</artifactId>
			<version>2.0</version>
		</dependency>
```

添加之后刷新，成功