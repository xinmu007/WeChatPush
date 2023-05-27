# 公众号配置
# 公众号appId
app_id = "wxf456a0e3a39dfc01"
# 公众号appSecret
app_secret = "7a1b6c135552da3c100e314b45950691"
# 模板消息id
# 每日消息
template_id1 = "OBxlMwEYgivoysmtDdjxsSxQEealzgzfyPVMphZhvSE"
# 课程消息,上课提醒
template_id2 = "DfmUpooeY9cbRrq571_h-5KJUuLFB5Sn3kfv5RT9_Xk"
# 晚安心语
template_id3 = "7E3K-8MKL9xn1X7EWO5cquzbaA8nHy5ac6XKwMtBqoE"
# 接收公众号消息的微信号
# 这是openid
user = ["oL7oo6CeEgl3AAaGQ7Sdk6BR2zPM"]

# 信息配置
# 所在省份
province = "广东"
# 所在城市
city = "广州"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如2000-1-1，---------倒计时
birthday = "2003-11-11"
# 放假日期，格式同上------------计时器
love_date = "2023-7-10"
# 天行数据晚安心语 key
good_Night_Key = "57702dff3d0abfb2b9b3a5ab3cf60454"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2023
month = 2
day = 20
# 每日推送时间
post_Time = "07:35:00"
# 每节课提醒时间（有课才会提醒）, 时:分:秒  的形式, 字符串, 根据个人需要设置几次
time_table = ["07:40:00", "11:02:50", "13:40:00", "15:30:00", "18:00:00", "19:40:00"]
# 课程时间
course_Time = ["8:10--9:50", "10:00--11:30", "14:00--15:30", "16:00--17:45", "19:00--20:45"]
# 晚安心语及第二天课程推送时间
good_Night_Time = "22:55:00"
# 课程表 "1"代表第一周，依次类推，根据个人实际课表添加，有几周就添加几周,
# 每一行代表一天, 例如  ['', '编译原理', '', '数据库原理及应用', '数据分析原理', '']  代表周一
classes = \
    {
        "11": [
            ['', '毛泽东思想和中国特色社会主义概论@八教303', '', '', '马克思主义中国化进程与青年担当@五教205', ''],
            ['大学英语@四教102', '高等数学@五教305', '离散数学@六教303', '', '', ''],
            ['', '程序设计基础课程综合实验@实训310', '', '习近平新时代特色社会主义概论@八教301', '大学生心理健康教育@八教512', ''],
            ['数据结构@六教304', '足球@第1足球场', '数据结构@实训408', '大学生职业发展与就业指导@二教205', '', ''],
            ['高等数学@五教305', '大学英语@四教102', '面向对象程序设计@实训306', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "12": [
            ['', '毛泽东思想和中国特色社会主义概论@八教303', '', '', '马克思主义中国化进程与青年担当@五教205', ''],
            ['大学英语@四教102', '高等数学@五教305', '离散数学@六教303', '', '', ''],
            ['', '程序设计基础课程综合实验@实训310', '', '习近平新时代特色社会主义概论@八教301',
             '大学生心理健康教育@八教512', ''],
            ['数据结构@六教304', '足球@第1足球场', '数据结构@实训408', '大学生职业发展与就业指导@二教205', '', ''],
            ['高等数学@五教305', '大学英语@四教102', '面向对象程序设计@实训306', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "13": [
            ['', '编译原理', '', '数据库原理及应用', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '数据挖掘实验', '数据挖掘实验'],
            ['', '计算机网络', '', '数据挖掘技术', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "14": [
            ['', '编译原理', '', '数据库原理及应用', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '数据挖掘实验', '数据挖掘实验'],
            ['', '计算机网络', '', '数据挖掘技术', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
    }

# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
