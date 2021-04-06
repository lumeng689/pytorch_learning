import torch

tensor = torch.rand(3, 4)

print(f"Shape of tensor: {tensor.shape}")

if torch.cuda.is_available():
    print("use cuda")
    tensor = tensor.to('cuda')

    tensor = torch.ones(4, 4)
    print(tensor)
    tensor[:, 1] = 0  # 将第1列(从0开始)的数据全部赋值为0
    print(tensor)

    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print(t1)

    # 逐个元素相乘结果
    print(f"tensor.mul(tensor): \n {tensor.mul(tensor)} \n")
    # 等价写法:
    print(f"tensor * tensor: \n {tensor * tensor}")

    print(f"tensor.matmul(tensor.T): \n {tensor.matmul(tensor.T)} \n")
    # 等价写法:
    print(f"tensor @ tensor.T: \n {tensor @ tensor.T}")
