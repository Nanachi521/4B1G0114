class Motorcycle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1  #品牌
        self.s2 = s2  #型號
        self.s3 = s3  #車色
        self.is_engine_on = False
        self.speed = 0

    def start_engine(self):
        if not self.is_engine_on:
            print(f" {self.s3} {self.s1} {self.s2}引擎啟動")
            self.is_engine_on = True
        else:
            print("引擎已啟動")

    def accelerate(self, speed_increase):
        if self.is_engine_on:
            self.speed += speed_increase
            print(f" {self.s3} {self.s1} {self.s2} 目前速度 {self.speed} km/h.")
        else:
            print("先發動引擎")

    def stop_engine(self):
        if self.is_engine_on:
            print(f" {self.s3} {self.s1} {self.s2}熄火")
            self.is_engine_on = False
            self.speed = 0
        else:
            print("已熄火")

# 創建一輛摩托車
my_motorcycle = Motorcycle("Kawasaki", "H2R", "黑/綠色")

# 操作摩托車
my_motorcycle.start_engine()

my_motorcycle.accelerate(220)
my_motorcycle.stop_engine()