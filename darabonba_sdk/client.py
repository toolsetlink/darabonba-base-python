# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
class Client:
    """
    @return timeRFC3339
    """
    def __init__(self):
        pass

    @staticmethod
    def time_rfc3339() -> str:
        raise Exception('Un-implemented')

    @staticmethod
    def generate_nonce() -> str:
        """
        @return: generateNonce
        @description 生成16位随机Nonce
        """
        raise Exception('Un-implemented')

    @staticmethod
    def generate_signature(
        body: str,
        nonce: str,
        secret_key: str,
        timestamp: str,
        uri: str,
    ) -> str:
        """
        @return: generateSignature
        @description 生成签名
        """
        raise Exception('Un-implemented')
