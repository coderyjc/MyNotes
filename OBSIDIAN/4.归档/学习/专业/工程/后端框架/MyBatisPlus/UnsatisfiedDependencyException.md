### 未满足的依赖

错误信息：

```text
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'certificationServiceImpl': Unsatisfied dependency expressed through field 'baseMapper': Error creating bean with name 'certificationMapper' defined in file [D:\code\github\certificate_analysis\certificate_analysis\backend\certificate\target\classes\top\coderyjc\certificate\mapper\CertificationMapper.class]: Unsatisfied dependency expressed through bean property 'sqlSessionFactory': Error creating bean with name 'sqlSessionFactory' defined in class path resource [com/baomidou/mybatisplus/autoconfigure/MybatisPlusAutoConfiguration.class]: Failed to instantiate [org.apache.ibatis.session.SqlSessionFactory]: Factory method 'sqlSessionFactory' threw exception with message: Failed to parse mapping resource: 'file [D:\code\github\certificate_analysis\certificate_analysis\backend\certificate\target\classes\mapper\IdentificationMapper.xml]'
```

最后这个原因找到了，是因为数据库的字段里有中文，mp无法映射mapper.xml文件

