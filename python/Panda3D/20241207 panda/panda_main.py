from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3


class MyPanda(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.environment = self.loader.load_model("models/environment")
        self.environment.setScale(
            0.25, 0.25, 0.25
        )  # 25%, not so huge Scale Up or Down your model
        self.environment.setPos(-8, 29, 0)
        self.environment.reparentTo(render)
        self.panda = Actor(
            "models/panda-model",
            {"walk": "models/panda-walk4", "idle": "models/panda-model"},
        )
        self.panda.setScale(0.005, 0.005, 0.005)  # 5%
        self.panda.reparentTo(render)
        # self.bamboo = self.loader.load_model("./bamboo.obj")
        # self.bamboo.setScale(0.01, 0.01, 0.01)
        # self.bamboo.setPos(-8, 4, 0)
        # self.bamboo.reparentTo(render)
        # self.music = self.loader.load_sfx("./soundtrack.mp3")  # load music or sound
        # self.chewing = self.loader.load_sfx("./chewing.mp3")
        # self.music.play()
        self.keyMap = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "turned": False,
        }  # for movements
        self.activities = {"eating": False}
        self.pandaIsTurning = False
        self.isPandaWalking = False
        self.pandaDegreeRotated = 0
        self.initial_panda_direction = "straight"
        self.accept("w", self.handleMovement, ["up", True])
        self.accept("w-up", self.handleMovement, ["up", False])
        self.accept("s", self.handleMovement, ["down", True])
        self.accept("s-up", self.handleMovement, ["down", False])
        self.accept("a", self.handleMovement, ["left", True])
        self.accept("a-up", self.handleMovement, ["left", False])
        self.accept("d", self.handleMovement, ["right", True])
        self.accept("d-up", self.handleMovement, ["right", False])
        self.accept("t", self.handleMovement, ["turned", True])
        self.accept("e", self.handleActivities, ["eating", True])
        # self.accept("e-up", self.handleActivities, ["eating", False])

        self.checkForMovement = self.taskMgr.add(
            self.update_game_loop, "update game loop"
        )
        self.checkForStop = self.task_mgr.add(
            self.checkForStop, "stop", delay=1
        )  # every sec

    def update_game_loop(self, task):
        dt = globalClock.getDt()  # datatime
        if self.pandaDegreeRotated < 180:
            self.update_keymap(-10.0, -10.0, dt)
        else:
            self.update_keymap(10.0, 10.0, dt)

        # if (
        #     self.activities["eating"]
        #     and self.panda.getX() > self.bamboo.getX() - 4
        #     and self.panda.getX() < self.bamboo.getX() + 4
        #     and self.panda.getY() < self.bamboo.getY() + 4
        #     and self.panda.getY() > self.bamboo.getY() - 4
        # ):
        #     (x, y, z) = self.panda.getScale()
        #     x += 0.000002
        #     y += 0.000002
        #     z += 0.000002
        #     self.panda.setScale(x, y, z)
        #     if self.chewing.status() == 1:
        #         self.chewing.play()
        # else:
        #     self.chewing.stop()

        if self.initial_panda_direction == "straight" and self.keyMap["turned"]:
            if self.pandaDegreeRotated < 180:
                if not self.isPandaWalking:
                    self.panda.loop("walk")
                    self.isPandaWalking = True
                    self.pandaIsTurning = True
                self.pandaDegreeRotated += 0.5
                self.panda.setHpr(self.pandaDegreeRotated, 0, 0)
            else:
                self.pandaIsTurning = False
        elif self.initial_panda_direction == "" and not self.keyMap["turned"]:
            if self.pandaDegreeRotated > 0:
                if not self.isPandaWalking:
                    self.panda.loop("walk")
                    self.isPandaWalking = True
                    self.pandaIsTurning = True
                self.pandaDegreeRotated -= 0.5
                self.panda.setHpr(self.pandaDegreeRotated, 0, 0)  # rotation
            else:
                self.panda.stop()
                self.initial_panda_direction = "straight"
                self.isPandaWalking = False
                self.pandaIsTurning = False
        return task.cont  # continiously

    def update_keymap(self, forward_or_backward, sideway, dt):
        if self.keyMap["up"]:
            if not self.isPandaWalking:
                self.panda.loop("walk")
                self.isPandaWalking = True
            self.panda.setPos(
                self.panda.getPos() + Vec3(0, forward_or_backward * dt, 0)
            )
        if self.keyMap["down"]:
            if not self.isPandaWalking:
                self.panda.loop("walk")
                self.isPandaWalking = True
            if self.pandaDegreeRotated < 180:
                self.panda.setPos(
                    self.panda.getPos() + Vec3(0, abs(forward_or_backward) * dt, 0)
                )
            else:
                self.panda.setPos(
                    self.panda.getPos() + Vec3(0, -forward_or_backward * dt, 0)
                )
        if self.keyMap["left"]:
            if not self.isPandaWalking:
                self.panda.loop("walk")
                self.isPandaWalking = True
            if self.pandaDegreeRotated < 180:
                self.panda.setPos(self.panda.getPos() + Vec3(abs(sideway) * dt, 0, 0))
            else:
                self.panda.setPos(self.panda.getPos() + Vec3(-sideway * dt, 0, 0))
        if self.keyMap["right"]:
            if not self.isPandaWalking:
                self.panda.loop("walk")
                self.isPandaWalking = True
            self.panda.setPos(self.panda.getPos() + Vec3(sideway * dt, 0, 0))

    def checkForStop(self, task):
        if (
            not self.keyMap["up"]
            and not self.keyMap["down"]
            and not self.keyMap["left"]
            and not self.keyMap["right"]
            and not self.pandaIsTurning
        ):
            self.panda.stop()
            self.isPandaWalking = False
        return task.cont

    def handleMovement(self, movement, value):
        if movement == "turned" and value and self.keyMap["turned"]:
            self.keyMap["turned"] = False
            self.initial_panda_direction = ""
        else:
            self.keyMap[movement] = value

    def handleActivities(self, activity, value):
        self.activities[activity] = value


game = MyPanda()
game.run()
