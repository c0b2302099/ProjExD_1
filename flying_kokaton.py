import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect() #練習8－1 （こうかとんRectを抽出）
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        if key_lst[pg.K_UP]:
            sum_mv[1] -= 2.5
            #kk_rct.move_ip([0, -1])
        if key_lst[pg.K_DOWN]:
            sum_mv[1] += 2.5
            #kk_rct.move_ip([0, +1])
        if key_lst[pg.K_LEFT]:
            sum_mv[0] -= 1
        #kk_rct.move_ip([-1, 0]) #演習課題1-1
        if key_lst[pg.K_RIGHT]:
            sum_mv[0] += 3
        sum_mv[0] -= 1
            #kk_rct.move_ip([2, 0]) #演習課題1-2
        kk_rct.move_ip(sum_mv)
        #key_lst = pg.key.get_rect()







        x = tmr%3200

        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_img2, [-x+1600, 0]) #練習7-1
        screen.blit(bg_img, [-x+3200, 0]) #練習7-2
        screen.blit(bg_img2, [-x+4800, 0]) #練習7-1


        screen.blit(kk_img, kk_rct)#練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200) # 練習5

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()