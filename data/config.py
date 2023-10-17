CRYPTO_TO_NETWORKS = {
    'USDT': ['BSC', 'Tron', 'Polygon', 'ETH', 'Avalanche C-Chain', 'Arbitrum One'],
    'BUSD': ['BSC', 'ETH'],
    'DAI': ['Polygon', 'BSC', 'ETH'],
    'USDC': ['Polygon', 'Tron', 'BSC', 'ETH', 'Avalanche C-Chain', 'Arbitrum One'],
    'ETH': ['Arbitrum One', 'ETH']
}


CRYPTO_TO_NETWORKS_IN_STATIC_WALLET = {
    'USDT': ['BSC', 'Tron', 'Polygon', 'ETH', 'Avalanche C-Chain', 'Arbitrum One'],
    'BUSD': ['BSC', 'Tron', 'ETH'],  # + 'Tron'
    'DAI': ['Polygon', 'BSC', 'ETH'],
    'USDC': ['Polygon', 'Tron', 'BSC', 'ETH', 'Avalanche C-Chain', 'Arbitrum One'],
    'ETH': ['BSC', 'Arbitrum One', 'ETH'],  # + 'BSC'
    'MATIC': ['Polygon', 'ETH']
}


CRYPTO_TO_NETWORKS_WITH_ONE_NETWORK = {
    'AVAX': 'AVALANCHE',  # 'Avalanche C-Chain'
    'BCH': 'BCH',  # 'Bitcoin cash'
    'BNB': 'BSC',
    'BTC': 'BTC',
    'CGPT': 'BSC',
    'DASH': 'DASH',
    'DOGE': 'DOGE',
    'LTC': 'LTC',
    'SOL': 'SOL',  # 'Solana',
    'TON': 'TON',
    'TRX': 'TRON',
    'VERSE': 'ETH',
    'XMR': 'XMR'  # 'Monero'
}


CRYPTO_TO_ADDRESS_WITH_ONE_NETWORK = {
    'AVAX': '0xa499fff7881db5ed170198f425f98b83da0c5516',
    'BCH': 'qz5s27t5g8md5rshjkdjr8fkrce54wwutcdae9u24j',
    'BNB': '0xa499fff7881db5ed170198f425f98b83da0c5516',
    'BTC': 'bc1qnhlnvmg6txw96ky8p9e7kg0t8jdptzhp05vv7j',
    'CGPT': '0xa499fff7881db5ed170198f425f98b83da0c5516',
    'DASH': 'XxGPu9QfukH3Ncg9TZCJavRV5ryrez46UL',
    'DOGE': 'DSgNv1WadH6GTAfXaGFG1Q2Jxd25BxTNLf',
    'LTC': 'ltc1qvcd0ulr6x7e2awz9av3emfa3wwv7vuna93x037',
    'SOL': 'DvLyVJZGm8Gn8vDWTPESick7vv6ECQY4yEcg95RxNCb2',
    'TON': 'EQCTdsh1uaafJEVsKU-7xrk7ltt76-k8h1uDDMJUOcOpf5zQ',
    'TRX': 'TLCse4jG8C4CW4Kv9QLVG7RM3YDTkBgKus',
    'VERSE': '0xa499fff7881db5ed170198f425f98b83da0c5516',
    'XMR': '84jZjEsE7qsSbyPbaWum8bjJKE8axUUGngdxjEoCET3WepP9vrhtzcCbWsbeGHJ7fRX4uCaLyp2DTFnqr65H5bNm5GrtZR7'
}