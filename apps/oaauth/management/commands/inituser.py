from django.core.management.base import BaseCommand
from apps.oaauth.models import OAUser, OADepartment
from rest_framework.response import Response


class Command(BaseCommand):
    def handle(self, *args, **options):
        boarder = OADepartment.objects.get(name='董事会')
        developer = OADepartment.objects.get(name='产品开发部')
        operator = OADepartment.objects.get(name='运营部')
        saler = OADepartment.objects.get(name='销售部')
        hr = OADepartment.objects.get(name='人事部')
        finance = OADepartment.objects.get(name='财务部')

        # 董事会的员工，都是superuser用户
        # 1. 李所长：属于董事会的leader
        lisuozhang = OAUser.objects.create_superuser(email="lisuozhang@qq.com", realname='李所长', password='111111', department=boarder)
        # 2. 李次长：董事会
        licizhang = OAUser.objects.create_superuser(email="licizhang@qq.com", realname='李次长', password='111111', department=boarder)
        # 3. 张章：产品开发部的leader
        zhangzhang = OAUser.objects.create_user(email="zhangzhang@qq.com", realname='张章', password='111111', department=developer)
        # 4. 李莉：运营部leader
        lili = OAUser.objects.create_user(email="lili@qq.com", realname='李莉', password='111111',
                                                   department=operator)
        # 5. 王武：人事部的leader
        wangwu = OAUser.objects.create_user(email="wangwu@qq.com", realname='王武', password='111111',
                                               department=hr)
        # 6. 赵柳：财务部的leader
        zhaoliu = OAUser.objects.create_user(email="zhaoliu@qq.com", realname='赵柳', password='111111',
                                                 department=finance)
        # 7. 孙琪：销售部的leader
        sunqi = OAUser.objects.create_user(email="sunqi@qq.com", realname='孙琪', password='111111',
                                                  department=saler)

        # 给部门指定leader和manager
        # 分管的部门
        # 李所长：产品开发部、运营部、销售部
        # 李次长：人事部、财务部
        # 1. 董事会
        boarder.leader = lisuozhang
        boarder.manager = None

        # 2. 产品开发部
        developer.leader = zhangzhang
        developer.manager = lisuozhang

        # 3. 运营部
        operator.leader = lili
        operator.manager = lisuozhang

        # 4. 销售部
        saler.leader = sunqi
        saler.manager = lisuozhang

        # 5. 人事部
        hr.leader = wangwu
        hr.manager = licizhang

        # 6. 财务部
        finance.leader = zhaoliu
        finance.manager = licizhang

        boarder.save()
        developer.save()
        operator.save()
        saler.save()
        hr.save()
        finance.save()

        self.stdout.write('初始用户创建成功！')
