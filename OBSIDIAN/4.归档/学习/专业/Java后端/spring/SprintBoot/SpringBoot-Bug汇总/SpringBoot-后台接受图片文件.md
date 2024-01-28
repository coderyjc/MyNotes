---
type: DeBug
skill: SpringBoot
create_date: 2022-01-31
---

#后端/JavaWeb #Java后端/SpringBoot #后端/Spring


后端接受 MultipartFile 类型的文件

前端使用XMLHttpRequest和formData 的时候不用自己指定contentType，而是可以让formdata封装好（会自动添加boundary）

这样后端就不会报错“is not multipart file ” 和 " boundary not found "

后端：

```java
/**
     * 更换头像
     * @return
     */
    @RequestMapping(value = "/upload/avatar", method = RequestMethod.POST)
    public Msg uploadAvatar(
            @RequestParam(value = "file") MultipartFile file,
            HttpServletRequest request
    ){
        // 登录状态
        String token = request.getHeader("token");
        if (null == token){
            return Msg.fail();
        }
        // 获取用户
        User user = (User) redisUtil.get(token);
        if (null == user){
            return Msg.expire();
        }
        // 文件判定
        if (null == file) {
            return Msg.fail().add("msg", "请选择要上传的图片");
        }
        if (file.getSize() > 1024 * 1024 * 10) {
            return Msg.fail().add("msg", "文件大小不能大于10M");
        }
        //获取文件后缀
        String suffix = Objects.requireNonNull(file.getOriginalFilename()).substring(file.getOriginalFilename().lastIndexOf(".") + 1);
        if (!"jpg,jpeg,gif,png".toUpperCase().contains(suffix.toUpperCase())) {
            return Msg.fail().add("msg", "请选择jpg,jpeg,gif,png格式的图片");
        }
        String savePath = null;
        try {
            savePath = new File(".").getCanonicalPath() + "\\\\target\\\\classes\\\\static\\\\avatar\\\\";
        } catch (IOException e) {
            e.printStackTrace();
        }

        File savePathFile = new File(savePath);
        if (!savePathFile.exists()) {
            //若不存在该目录，则创建目录
            savePathFile.mkdir();
        }

        //用户头像名称就是用户的id
        String filename = user.getUserId() + "." + suffix;

        try {
            //将文件保存指定目录
            file.transferTo(new File(savePath + filename));
        } catch (Exception e) {
            e.printStackTrace();
            return Msg.fail().add("msg", "保存文件异常");
        }

//        //返回文件名称
        return Msg.success().add("suc", true);
    }
```

前端

```jsx
uploadImg(type) {
      let _this = this
      if (type === 'blob') {
        //获取截图的blob数据
        this.$refs.cropper.getCropBlob(async (data) => {
          let formData = new FormData()
          formData.append('file', data, 'file.png')
          //调用接口上传
          const ajax = new XMLHttpRequest()
          ajax.open('POST', '<http://localhost:8080/user/upload/avatar>', true)
          ajax.setRequestHeader("token", getToken())
          ajax.send(formData)
          ajax.onreadystatechange = function () {

          }
        })
      }
    },
```