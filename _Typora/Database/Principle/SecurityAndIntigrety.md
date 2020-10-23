## SecurityAndIntegrity

### Trigger（5th 6:37 and 6th）

数据库中的约束有两大类：静态约束（数据库的状态、必须满足的条件）和动态约束（数据库的状态转换过程中的条件）

Trigger解决的是动态的约束->状态转换时应该遵守的规则或者行为

我们有的时候希望数据库有一定的主动能力，当数据库具有某个状态的时候，自动触发某种操作。

Trigger: procedure that starts automatically if specified changes occur to the DBMS

Three parts:

- Event (activates the trigger) 事件

- Condition (tests whether the triggers should run) 条件

- Action (what happens if the trigger runs) 动作

Active database rules (ECA rules)

触发器由ECA规则组成的。

具有触发器的数据库叫做主动数据库。

```sql
CREATE TRIGGER youngSailorUpdate -- 创建一个触发器名字叫 youngSailorUpdate
AFTER INSERT ON SAILORS 
-- AFTER：触发的时机是在操作执行之前还是之后(BEFORE: 之前)
-- INSTER: 监视插入操作
-- SAILOR: 监视 SAILORS 这张表

REFERENCING NEW TABLE NewSailors -- 我把新插入的元组看成一张表并且起名字叫NewSailors
-- REFERENCING: 对过渡值的引用。
-- 对于引用的这个过渡值，把它看成一张表，NEW 表示引用的是新值，（OLD 表示旧值）
-- NewSailors 是我给它起的新名字
/*
	当我们在对数据库中的某张表做插删改操作的时候，在这些操作的执行过程中，数据库里面被修改的数据的值会从原来的旧值变换为新值，在变换过程中的值叫做过渡值，在触发器的定义过程中我可能需要引用这个过渡值。
*/

FOR EACH STATEMENT -- 表示我检查的‘力度’ 是语句，还是元组
-- 这里还可以在后面加上一个 WHEN 子句，表示“只有在满足WHEN条件的时候才去做以下的操作”，所以也可以在这一句里对新插入的值的年龄进行判断，如果满足小于18就插入到YoungSailors中去
-- 对每一条 INSERT 语句（STATEMENT），我要做以下的动作。
-- FOR RACH ROW 对被我更新或者删除的元组进行操作。

INSERT 
	INTO YoungSailors(sid, name, age, rating) -- 插入到YoungSailors表中
	SELECT sid, name, age, rating
	FROM NewSailors N  -- 把我新插入的元组看成一张表，查看其年龄是否符合规定，如果符合就插入到YoungSailors表中
	WHERE N.age <= 18;

```

Execution of Rules（ECA执行规则，不同的数据库的执行规则可能不同）

- Immediate execution（立即执行）

- Deferred execution（延迟执行，有的数据库认为当一条SQL语句执行完毕之后会触发另外一个触发器，从而抵消掉这个SQL语句的执行情况，所以等到所有的语句执行完毕，将要commit的时候再看哪些规则需要做）

- Decoupled or detached mode

- Cascading trigger
    - Control nested execution of rules

    - Prevent nontermination

        - Triggering graph

        - Specify the upper limit of cascading times

    - So triggers should be used reasonably



Implementation of ECA
Loosely coupling
Tightly coupling (DB2, Oracle, etc.)
Nested method
The rules are nested into transaction and executed by DBMS as a part of the transaction.
Grafting method
Query modification method