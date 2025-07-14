import React from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import { useState } from 'react';
import axios from 'axios';
import '../index.css'
import { redirect } from "react-router-dom"
import { useNavigate } from 'react-router-dom';




const Registr = () => {


  
  const onFinish = (values) => {
    CheckUserRegistr(values['email'],values['password'],values['username'])
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };


  const navigate = useNavigate();

  const redirect_home = () => {
    navigate('/')
  }

  

  
  function CheckUserRegistr(email_user,password_user,username_user) {
    const params = new URLSearchParams();
    params.append('username', username_user);
    params.append('password', password_user);
    params.append('email', email_user);
    
    axios.post(
      'http://127.0.0.1:8000/auth/jwt/register', 
      params,
      { withCredentials: true }
      ).then(
        r =>  {
          if (r.status == 201){
            axios.post(
                'http://127.0.0.1:8000/auth/jwt/login', 
                params,
                { withCredentials: true }
                ).then(
                  r =>  {
                    if (r.status == 204){
                      return(redirect_home())
                    }
                  }
                ).catch((error) => {
                    alert('Неправильное имя пользователя или пароль')
                  }
                )
          }
        }
      ).catch((error) => {
          alert('Пользователь с таки email уже существует')
        }
      )
    
    
  
  }

  return(
    <div className="container">
      <div className='auth-form'>
        <Form
          name="basic"
          labelCol={{
            span: 8,
          }}
          wrapperCol={{
            span: 16,
          }}
          style={{
            maxWidth: 600,
          }}
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="email"
            name="email"
            id='email'
            
            rules={[
              {
                required: true,
                message: 'Please input your email!',
              },
            
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="username"
            name="username"
            id='username'
            
            rules={[
              {
                required: true,
                message: 'Please input your username!',
              },
            
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            id='password'
            rules={[
              {
                required: true,
                message: 'Please input your password!',
              },
            ]}
            
          >
            <Input.Password />
          </Form.Item>

          <Form.Item
            name="remember"
            valuePropName="checked"
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Checkbox>Remember me</Checkbox>
          </Form.Item>

          <Form.Item
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </div>
    </div>

  )
};
export default Registr;