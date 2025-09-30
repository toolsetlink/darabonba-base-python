# -*- coding: utf-8 -*-
import unittest
import re
import hashlib
from darabonba_base_python.client import Client


class TestClient(unittest.TestCase):
    
    def test_time_rfc3339(self):
        """测试time_rfc3339方法返回的时间字符串格式是否符合RFC3339标准"""
        # 调用方法获取结果
        result = Client.time_rfc3339()
        
        # 验证返回值是否为字符串类型
        self.assertIsInstance(result, str)
        
        # 验证格式是否符合RFC3339标准 (YYYY-MM-DDTHH:MM:SS.XXXZ)
        pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'
        self.assertTrue(re.match(pattern, result), f"返回的时间格式不符合RFC3339标准: {result}")
    
    def test_generate_nonce(self):
        """测试generate_nonce方法是否返回16位的十六进制随机字符串"""
        # 调用方法获取结果
        result = Client.generate_nonce()
        
        # 验证返回值是否为字符串类型
        self.assertIsInstance(result, str)
        
        # 验证字符串长度是否为16
        self.assertEqual(len(result), 16)
        
        # 验证是否只包含十六进制字符
        try:
            # 尝试将字符串转换为十六进制值，如果成功则说明是有效的十六进制字符串
            int(result, 16)
        except ValueError:
            self.fail(f"返回的nonce不是有效的十六进制字符串: {result}")
            
    def test_generate_signature(self):
        """测试generate_signature方法是否按照指定规则正确生成MD5签名"""
        # 测试用例1：包含所有参数
        body = "test_body"
        nonce = "abcdef1234567890"
        secret_key = "test_secret_key"
        timestamp = "2023-01-01T00:00:00.000Z"
        uri = "/test/uri"
        
        # 调用方法获取结果
        result = Client.generate_signature(body, nonce, secret_key, timestamp, uri)
        
        # 手动计算预期结果进行验证
        expected_parts = [
            f"body={body}",
            f"nonce={nonce}",
            f"secretKey={secret_key}",
            f"timestamp={timestamp}",
            f"url={uri}"
        ]
        expected_sign_str = "&".join(expected_parts)
        expected_md5 = hashlib.md5(expected_sign_str.encode('utf-8')).hexdigest()
        
        # 验证生成的签名是否正确
        self.assertEqual(result, expected_md5)
        
        # 测试用例2：body为空字符串
        empty_body = ""
        result_empty_body = Client.generate_signature(empty_body, nonce, secret_key, timestamp, uri)
        
        # 手动计算预期结果进行验证
        expected_parts_empty_body = [
            f"nonce={nonce}",
            f"secretKey={secret_key}",
            f"timestamp={timestamp}",
            f"url={uri}"
        ]
        expected_sign_str_empty_body = "&".join(expected_parts_empty_body)
        expected_md5_empty_body = hashlib.md5(expected_sign_str_empty_body.encode('utf-8')).hexdigest()
        
        # 验证生成的签名是否正确
        self.assertEqual(result_empty_body, expected_md5_empty_body)
        
        # 测试用例3：body为None
        none_body = None
        result_none_body = Client.generate_signature(none_body, nonce, secret_key, timestamp, uri)
        
        # 手动计算预期结果进行验证
        expected_parts_none_body = [
            f"nonce={nonce}",
            f"secretKey={secret_key}",
            f"timestamp={timestamp}",
            f"url={uri}"
        ]
        expected_sign_str_none_body = "&".join(expected_parts_none_body)
        expected_md5_none_body = hashlib.md5(expected_sign_str_none_body.encode('utf-8')).hexdigest()
        
        # 验证生成的签名是否正确
        self.assertEqual(result_none_body, expected_md5_none_body)