# java.cc.ryanc.halo 0.0.1

## model 

### domain

#### User.java

`@Data` 相当于 `@Getter @Setter @RequiredArgsConstructor @ToString @EqualsAndHashCode`这5个注解的合集。

`@Entity`一般和`@Table(name = "halo_user")`一起使用

@Entity是指这个类映射到数据库表， 当你不使用这个类（被注解的类）时，后台不会对其进行处理，只有当你从数据库读取数据时，由于你要读取的表映射有实体类（被@Entity注释的）， 那么后台应该会自动帮你实例化一个对象， 然后将数据库中的数据填充到对象中





### dto


### tag





## repository



## config









## util


## web




