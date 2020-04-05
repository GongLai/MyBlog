# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.models import User


class LoginFrom(FlaskForm):
    """当你在当前表格没有输入而直接到下一个表格时会提示你输入"""
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入用户名')])
    remember_me = BooleanField('记住我', default=False)
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    """注册"""
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    password2 = PasswordField('重复密码', validators=[DataRequired(message='两次密码输入不一致，请重新输入'), EqualTo('password')])
    email = StringField('邮箱', validators=[DataRequired(message='请输入邮箱'), Email()])
    submit = SubmitField('注册')

    # 校验用户是否重复注册
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名重复，请您重新换一个！')

    # 校验邮箱是否重复
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱重复，请您重新换一个！')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名！')])
    about_me = TextAreaField('关于我', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')
