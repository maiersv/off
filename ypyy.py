import random
import time
import vk
import vk_api

y=1

while y<1000:
    vk_session = vk_api.VkApi(token='51b1d07872298a5a89ec4df034ccc8605bca2ca6853fd949822a779b1ff1db8cb4d01d336d8ce2645ff3b')

    vk = vk_session.get_api()
    print(vk.wall.createComment(owner_id=565524195,post_id=325,sticker_id=126))
    y=y+1
    time.sleep(2)

import random
import time
import vk
import vk_api

y=1

while y<1000:
    vk_session = vk_api.VkApi(token='51b1d07872298a5a89ec4df034ccc8605bca2ca6853fd949822a779b1ff1db8cb4d01d336d8ce2645ff3b')

    vk = vk_session.get_api()
    print(vk.wall.createComment(owner_id=542741920,post_id=164,sticker_id=126))
    y=y+1
    time.sleep(2)
