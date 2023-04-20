
```ad-note
官网：http://doc.wupaas.com/docs/easypoi
```

## 添加注解

SpringBoot项目只需要添加boot-starter即可

```xml
        <!-- https://mvnrepository.com/artifact/cn.afterturn/easypoi-spring-boot-starter -->
        <dependency>
            <groupId>cn.afterturn</groupId>
            <artifactId>easypoi-spring-boot-starter</artifactId>
            <version>4.4.0</version>
        </dependency>
```


## 定义DTO

在DTO中使用`@Excel`注解，平时也只需要使用这一个注解即可

更多的注解[在这里查看](http://doc.wupaas.com/docs/easypoi/easypoi-1c0u96flii98v)

### 导入的DTO

```java
package top.coderyjc.certificate.model.dto;

import cn.afterturn.easypoi.excel.annotation.Excel;
import com.baomidou.mybatisplus.annotation.TableField;
import lombok.Data;

import java.sql.Date;

/**
 * ClassName: CertificationImportDTO
 * Package: top.coderyjc.certificate.model.dto
 * Description:
 *
 * @Author Yan Jingcun
 * @Create 4/8/2023 8:10 PM
 * @Version 1.0
 */
@Data
public class CertificationImportDTO {

    /**
     * 姓名
     */
    @TableField("name")
    @Excel(name = "姓名")
    private String name;

    /**
     * 身份证号
     */
    @Excel(name = "身份证号")
    @TableField("identification_id")
    private String identificationId;

    /**
     * 面试年份
     */
    @Excel(name = "面试年份")
    @TableField("interview_year")
    private String interviewYear;

    /**
     * 合格证号
     */
    @Excel(name = "合格证号")
    @TableField("qualification_id")
    private String qualificationId;

    /**
     * 专业
     */
    @Excel(name = "专业")
    @TableField("major")
    private String major;

    /**
     * 有效期
     */
    @Excel(name = "有效期", format = "yyyy-MM-dd")
    @TableField("validate_date")
    private Date validateDate;
}
```

### 导出的DTO

导出的DTO使用原始的即可;

```java
package top.coderyjc.certificate.model.entity;

import cn.afterturn.easypoi.excel.annotation.Excel;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.util.Date;


import lombok.Data;

/**
 * <p>
 * 证书表哦
 * </p>
 *
 * @author Yan Jingcun
 * @since 2023-04-02
 */
@Data
@TableName("tbl_certification")
public class Certification implements Serializable {

    /**
     * 主键，无意义，自增
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    /**
     * 姓名
     */
    @TableField("name")
    @Excel(name = "姓名", width = 10)
    private String name;

    /**
     * 身份证号
     */
    @Excel(name = "身份证号", width = 20)
    @TableField("identification_id")
    private String identificationId;

    /**
     * 面试年份
     */
    @Excel(name = "面试年份", suffix = "年", width = 8)
    @TableField("interview_year")
    private String interviewYear;

    /**
     * 合格证号
     */
    @Excel(name = "合格证号", width = 15)
    @TableField("qualification_id")
    private String qualificationId;

    /**
     * 专业
     */
    @Excel(name = "专业", width = 25)
    @TableField("major")
    private String major;

    /**
     * 有效期
     */
    @Excel(name = "有效期", format = "yyyy-MM-dd", width = 15)
    @TableField("validate_date")
    private Date validateDate;

    /**
     * 性别
     */
    @Excel(name = "性别", width = 8, replace = { "男_1", "女_0" })
    @TableField("gender")
    private Integer gender;

}
```

## 导出数据

导出的时候直接将数据写到response中即可。

### Controller

```java
@RequestMapping(value = "/export", method = RequestMethod.GET)
    public void exportExcel(
            HttpServletResponse response,
            @RequestParam(value = "exportColumn[]", defaultValue = "") List<String> exportColumn,
            @RequestParam(value = "exportId[]", defaultValue = "") List<String> exportId,
            @RequestParam(value = "searchCondition", defaultValue = "{}") String searchCondition
    ) {
        JSONObject condition = JSONObject.parseObject(searchCondition);
        service.exportExcel(response, exportId, exportColumn, condition);
    }
```

在以上的控制器函数中，exportColumn是选择导出列，exportId和searchCondition是筛选导出的行。

这里直接调用了service的函数

### Service

```java
@Override
    public void exportExcel(HttpServletResponse response, List<String> exportId, List<String> exportColumn, JSONObject condition) {

        List<Certification> list = null;
        QueryWrapper<Certification> wrapper = new QueryWrapper<>();

//      查找数据
        if(exportId.size() > 0){
//            按照id导出
            list = baseMapper.selectBatchIds(exportId);
        }
        else if(condition.size() > 0){
            if(!condition.get("name").equals(""))  wrapper.eq("name", condition.get("name"));
            if(!condition.get("identificationId").equals(""))  wrapper.eq("identification_id", condition.get("identificationId"));
            if(!condition.get("interviewYear").equals(""))  wrapper.eq("interview_year", condition.get("interviewYear"));
            if(!condition.get("qualificationId").equals(""))  wrapper.eq("qualification_id", condition.get("qualificationId"));
            if(!condition.get("major").equals(""))  wrapper.eq("major", condition.get("major"));
            if(!condition.get("validateDate").equals(""))  wrapper.eq("validate_date", condition.get("validateDate"));
            if(!condition.get("gender").equals(""))  wrapper.eq("gender", condition.get("gender"));
            list = baseMapper.selectList(wrapper);
        }

// list是查找完成的需要导出的数据列表

//        动态导出的列名
        List<ExcelExportEntity> exportEntityList = new ArrayList<>();
        if(exportColumn.contains("姓名")){
            ExcelExportEntity nameEntity = new ExcelExportEntity("姓名", "name");
            nameEntity.setWidth(10);
            exportEntityList.add(nameEntity);
        }
        if(exportColumn.contains("身份证号")){
            ExcelExportEntity identificationIdEntity = new ExcelExportEntity("身份证号", "identificationId");
            identificationIdEntity.setWidth(20);
            exportEntityList.add(identificationIdEntity);
        }
        if(exportColumn.contains("面试年份")){
            ExcelExportEntity interviewYearEntity = new ExcelExportEntity("面试年份", "interviewYear");
            interviewYearEntity.setWidth(8);
            exportEntityList.add(interviewYearEntity);
        }
        if(exportColumn.contains("合格证号")){
            ExcelExportEntity qualificationIdEntity = new ExcelExportEntity("合格证号", "qualificationId");
            qualificationIdEntity.setWidth(15);
            exportEntityList.add(qualificationIdEntity);
        }
        if(exportColumn.contains("专业")){
            ExcelExportEntity majorEntity = new ExcelExportEntity("专业", "major");
            majorEntity.setWidth(25);
            exportEntityList.add(majorEntity);
        }
        if(exportColumn.contains("有效期")){
            ExcelExportEntity validateDateEntity = new ExcelExportEntity("有效期", "validateDate");
            validateDateEntity.setWidth(15);
            validateDateEntity.setFormat("yyyy-MM-dd");
            exportEntityList.add(validateDateEntity);
        }
        if(exportColumn.contains("性别")){
            ExcelExportEntity genderEntity = new ExcelExportEntity("性别", "gender");
            genderEntity.setWidth(8);
            genderEntity.setReplace(new String[]{ "男_1", "女_0" });
            exportEntityList.add(genderEntity);
        }

        DownloadUtil.downloadExcel(response, new ExportParams(), exportEntityList, Certification.class, list);
    }
```

---

导出动态列的时候，使用以下语句定义导出列

```java
List<ExcelExportEntity> exportEntityList = new ArrayList<>();
```

使用ExcelExportEntity定义导出列的属性，构造函数中两个参数分别是实体类的注解中的列名和属性名。

Excel导出实体类的属性也就是Excel表格的属性，和实体类中的属性是相同的。

```java
@Excel(name = "性别", width = 8, replace = { "男_1", "女_0" })
private Integer gender;
```

```java
ExcelExportEntity genderEntity = new ExcelExportEntity("性别", "gender");
genderEntity.setWidth(8);
genderEntity.setReplace(new String[]{ "男_1", "女_0" });
exportEntityList.add(genderEntity);
```

从上面可以看出，属性是对应的。

```java
DownloadUtil.downloadExcel(response, new ExportParams(), exportEntityList, Certification.class, list);
```

构造完成导出的实体类列表之后，直接调用Excel下载函数。

### DownloadExcel

```java
public static void downloadExcel(HttpServletResponse response, ExportParams entity, List<ExcelExportEntity> exportColumns, Class<?> pojoClass, Collection<?> dataSet) {
//      目录是cache（缓存），文件名暂时用时间戳代替
        String directory = "./cache";
        String fileName = System.currentTimeMillis() + ".xlsx";

//      获取临时导出目录
        File file = new File(directory);
        if(!file.exists()) file.mkdir();

//      创建表格文件
        Workbook workbook = ExcelExportUtil.exportExcel(entity, exportColumns, dataSet);

//      导出文件到指定位置
        FileOutputStream outputStream = null;
        try {
            outputStream = new FileOutputStream(directory + '\\' + fileName);
            workbook.write(outputStream);
            outputStream.close();
            workbook.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

//      返回给客户端
        downloadFile(response, fileName, directory);
    }

```

这里生成创建了Excel文件到了缓存文件夹中。最后调用了downloadFile将文件传输到客户端。

### DownloadFile

文件下载工具。

```java
    public static void downloadFile(HttpServletResponse response, String fileName, String directory){
        File file = new File(directory + "/" + fileName);
        if(file.exists()){ //判断文件父目录是否存在
            response.setContentType("application/vnd.ms-excel;charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
            response.setHeader("Content-Disposition", "attachment;fileName=" + java.net.URLEncoder.encode(fileName, StandardCharsets.UTF_8));
            response.setHeader("Content-Length", "" + file.length());
            byte[] buffer = new byte[1024];
            FileInputStream fis = null;
            BufferedInputStream bis = null;
            OutputStream os = null; //输出流
            try {
                os = response.getOutputStream();
                fis = new FileInputStream(file);
                bis = new BufferedInputStream(fis);
                int i = bis.read(buffer);
                while(i != -1){
                    os.write(buffer);
                    i = bis.read(buffer);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            try {
                assert bis != null;
                bis.close();
                fis.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

```

## 导入数据

### Controller

```java
@RequestMapping(value = "/importExcel", method = RequestMethod.POST, headers = "content-type=multipart/form-data")
    public Msg importExcel(@RequestParam("file") MultipartFile file) {

        //文件为空校验
        if (file == null) {
            return Msg.fail().add("msg", "文件为空");
        }

        //文件后缀名校验
        String fileName = file.getOriginalFilename();
        if (!(fileName.endsWith("xls") || fileName.endsWith("xlsx"))) {
            return Msg.fail().add("msg", "上传文件格式不正确，请传入正确的Excel文件");
        }

        String msg;
        try {
            msg = service.importExcel(file);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return Msg.success().add("msg", msg);
    }
```

### Service

```java
@Override
    public String importExcel(MultipartFile file) throws Exception {
        //需保存到数据库的记录
        List<Certification> resultData = new ArrayList<>();
        ImportParams params = new ImportParams();
        // 表头设置为首行
        params.setHeadRows(1);
        params.setTitleRows(0);

        ExcelImportResult<CertificationImportDTO> result;
        result = ExcelImportUtil.importExcelMore(file.getInputStream(), CertificationImportDTO.class, params);

        List<CertificationImportDTO> correctResultList = result.getList();

        for (CertificationImportDTO certificationImportDTO : correctResultList) {
            Certification certification = new Certification();
            BeanUtils.copyProperties(certificationImportDTO, certification);
            certification.setGender(Integer.parseInt(certification.getIdentificationId().substring(16,17)) % 2);
            resultData.add(certification);
        }

        saveBatch(resultData);
        return "导入成功";
    }

```