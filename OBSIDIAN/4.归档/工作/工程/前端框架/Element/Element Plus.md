### 使用表单校验

==配置型校验==

假设表格的模型为 form

在el-form中设置`model`和`rules`，rules要校验的项目写在表单子项的`prop`中。

```html
<el-form :model="form" :rules="rules">
      <el-form-item label="姓名" prop="name">
        <el-input v-model="form.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="准考证号" prop="examId">
        <el-input v-model="form.examId" autocomplete="off" />
      </el-form-item>
</el-form>
```

```js
 setup(props, { emit }) {
	// 这里的name和examId对应的是
    const getRules = () => ({
      name: [
        { required: true, message: '请输入姓名', trigger: 'blur', },
      ],
      examId: [
        { required: true, message: '请输入准考证号', trigger: 'blur', },
        { min: 10, max: 10, message: '准考证号的长度为10位', trigger: 'blur', },
      ],
    })

	const state = reactive({
      form: {
        name: "",
        examId: "",
	  },
	  rules: getRules(),
	})

	return {
      ...toRefs(state),
    }
```

==正则校验==

在校验规则中设置 `pattern` 即可

```js
{ 
  pattern: /^\d{6}$/, 
  message: '请输入合法的验证码', 
  trigger: 'blur' 
}
```

==自定义规则校验==

假设表格的模型为 form

在el-form中设置`model`和`rules`，rules要校验的项目写在表单子项的`prop`中。

在rule中添加validator，其为一个函数，函数必须返回callback

在 `callback(new Error('请输入教育心理学成绩'))` 为抛出了message

```js
setup(props, { emit }) {
	// 这里的name和examId对应的是
    const getRules = () => ({
      name: [
        { required: true, message: '请输入姓名', trigger: 'blur', },
      ],
      examId: [
        { required: true, message: '请输入准考证号', trigger: 'blur', },
        { min: 10, max: 10, message: '准考证号的长度为10位', trigger: 'blur', },
      ],
      educationPsychologyScore : [
        { 
          validator:  (rule, value, callback) => {
            if (state.form.educationPsychologyStatus == '正常' && !value) {
              callback(new Error('请输入教育心理学成绩'))
            } else {
              callback()
            } 
          },
          trigger: 'blur'
        }
      ],
    })

	const state = reactive({
      form: {
        name: "",
        examId: "",
	  },
	  rules: getRules(),
	})

	return {
      ...toRefs(state),
    }
```


==提交表单时的兜底验证==

先不写了。

