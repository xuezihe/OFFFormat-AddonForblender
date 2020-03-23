# OFF文件规范化脚本
import linecache
import os

def get_pointnum(filename,line_number):
    '''
    输入文件名,off行数行
    输出有效点行数
    :param filename，line_nunber:
    :return total_line:
    '''
    context=linecache.getline(filename,line_number)
    # print(context)
    total_line=context.split(" ")[0]

    return total_line



def get_path(path, suffix_name, *args):
    """深度遍历获取所有后缀名为suffix_name的文件列表，可接收多个后缀名"""
    # 获取当前目录下的所有文件
    path_list=[]
    path_name=[]
    dir_list = os.listdir(path)
    # print(dir_list)
    for file in dir_list:
        # 遍历所有文件
        # print(os.path.abspath(path))
        # print(file)
        # 将文件绝对路径和文件名拼接
        file_path = os.path.join(os.path.abspath(path), file)
        # print(file_path)
        if os.path.isdir(file_path):
            # 若当前文件为文件夹，重新遍历当前文件夹
            # print("测试")
            get_path(file_path, suffix_name, *args)
        else:
            if file_path.endswith(suffix_name):
                # 若文件后缀名为suffix_name则存储文件绝对路径
                    path_name.append(file)
                    path_list.append(file_path)
            if len(args):
                # 若查找多个后缀名的文件，遍历需要查询的文件后缀
                for arg in args:
                    if file_path.endswith(arg):
                        # 若找到文件后缀为arg的存储文件的绝对路径
                        path_list.append(file_path)
                        path_name.append(file)
    return path_list,path_name


if __name__ == '__main__':

    unit_r=10 #单位圆半径



    # total_line=get_pointnum('test.off',2)
    datapath=r'C:\Users\Xue\Desktop\ML\3dviewgraph\evaldatasetpath\smalldataset_off'
    off_path,off_name=get_path(path=datapath,suffix_name='off')
    print(off_path)
    print(off_name)


    for a in range(len(off_path)):
        edit_name=''.join([str(unit_r),'edit_',off_name[a]])



        total_r = []
        new_x = []
        new_y = []
        new_z = []
        max_r = 0

        with open(off_path[a],'r') as f:
            with open(edit_name, 'w+') as ff:
                total_line=get_pointnum(off_path[a],2)
                print(total_line)
                lines=f.readlines()
                for i in lines[2:int(total_line)+2]: #计算每个顶点的r的大小，存入total_r列表中
                    x=i.split(" ")[0]
                    y=i.split(" ")[1]
                    z=i.split(" ")[2]
                    # print(x,'\n',y,'\n',z)
                    # print(type(x))
                    r=(float(x)**2+float(y)**2+float(z)**2)**0.5
                    total_r.append(r)
                max_r=total_r[0]
                for r in range(0,len(total_r)):#获得最大max_r
                    if max_r <total_r[r]:
                        max_r=total_r[r]
                for i in lines[2:int(total_line)+2]:#计算每个顶点的r的大小，存入total_r列表中,设单位圆半径为10
                    x=i.split(" ")[0]
                    y=i.split(" ")[1]
                    z=i.split(" ")[2]
                    x=float(x)/(max_r/unit_r)
                    y=float(y)/(max_r/unit_r)
                    z=float(z)/(max_r/unit_r)
                    # print('x:',new_x)
                    # print('y',new_y)
                    # print('z',new_z)
                    new_x.append(x)
                    new_y.append(y)
                    new_z.append(z)
                line_2=linecache.getline(off_path[a],2)
                print(line_2)
                ff.write('OFF \n') #开始写edit新文件
                ff.write(line_2)
                for i in range(len(new_x)):
                    ff.write(str(new_x[i]))
                    ff.write(' ')
                    ff.write(str(new_y[i]))
                    ff.write(' ')
                    ff.write(str(new_z[i]))
                    ff.write('\n')
                for l in range(len(lines)):
                    if l > int(total_line)+1:
                        # print(int(total_line)+1)
                        current_line=lines[l]
                        # print(current_line)
                        ff.write(current_line)
                    else:
                        continue

    print('line_2',line_2,'total_line',total_line)




