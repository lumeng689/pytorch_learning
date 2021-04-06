'''
需要安装 pybullet
pip install pybullet
'''
import pybullet
import pybullet_data

datapath = pybullet_data.getDataPath()
pybullet.connect(pybullet.GUI)
pybullet.setAdditionalSearchPath(datapath)
pybullet.loadURDF("r2d2.urdf", [0, 0, 1])
