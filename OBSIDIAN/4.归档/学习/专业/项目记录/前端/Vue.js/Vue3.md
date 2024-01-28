
### 使用slot的时候拿不到scope和row的数据

插槽的值不会热更新和热部署，刷新一下就可以拿到row值

原来的code：

字段配置：

```js
        {
          label: 'public.operate',
          width: 100,
          align: 'center',
          fixed: 'right',
          tdSlot: 'operate', // 自定义单元格内容的插槽名称
        },
```

slot：

```html
    <template #operate="{ row }">
      <el-button size="small" type="danger" @click="deleteScore(row.id)">
        {{ $t('public.delete') }}
      </el-button>
    </template>
```

