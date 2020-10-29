import os

class BotConfig:
    try:
        token = os.environ.get("TOKEN", "758275539:AAHx-T_3ykyFL2ND4L5UhdR15fJebspaiqw")
    except Exception as e:
        print('BotConfig error: %s' % str(e))