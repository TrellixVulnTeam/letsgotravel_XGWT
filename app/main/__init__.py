# -*- coding: utf-8 -*-
# 创建蓝本
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,error
from ..models import Permission

# 把Permission类加入模板上下文
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)