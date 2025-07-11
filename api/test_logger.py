#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.log_utils import logger, setup_logger

def test_function():
    """测试函数，用于演示日志输出"""
    logger.info("这是一条信息日志")
    logger.warning("这是一条警告日志")
    logger.error("这是一条错误日志")
    
    # 嵌套函数调用，测试堆栈信息
    nested_function()

def nested_function():
    """嵌套函数，用于测试堆栈信息"""
    logger.debug("这是一条来自嵌套函数的调试日志")
    try:
        # 故意引发异常
        result = 1 / 0
    except Exception as e:
        logger.exception(f"捕获到异常: {e}")

def test_custom_config():
    """测试自定义日志配置"""
    # 创建一个自定义配置的logger
    custom_logger = setup_logger(
        log_level="DEBUG",
        log_file="logs/test.log"
    )
    
    custom_logger.debug("这是一条使用自定义配置的调试日志")
    custom_logger.info("这条日志会同时输出到控制台和文件")

if __name__ == "__main__":
    logger.info("开始测试日志工具")
    
    # 测试基本日志功能
    test_function()
    
    # 测试自定义配置
    test_custom_config()
    
    logger.info("日志测试完成") 