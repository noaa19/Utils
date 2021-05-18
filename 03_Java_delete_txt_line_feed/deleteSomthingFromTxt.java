/**
 * 删除文本内的多余换行
 */

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class deleteSomthingFromTxt {

    public static void main(String[] args) {

        //写入原始文件完整路径名
        File file=new File("D:\\文件夹\\我的原始文本.txt");
        InputStream is=null;
        BufferedReader br = null;
        String tmp;
        FileWriter writer=null;
        try {
            is=new BufferedInputStream(new FileInputStream(file));
            br = new BufferedReader(new InputStreamReader(is, "utf-8"));
            /**
             * 补充更改后文件完整路径名，
             * 例如D:\\文件夹\\我的最终文本.txt
             * FileWriter会创建或者覆写这个文件
             * 如果不希望覆写，而想要在原文内容后追加
             * 请改为FileWriter("D:\\文件夹\\我的最终文本.txt",true);
             */
            writer = new FileWriter("D:\\文件夹\\我的最终文本.txt");

            /**
             * 核心功能代码部分
             * if里面的内容可以任意更换
             * 但只能匹配readline()，也就是一行里的内容
             */
            while((tmp=br.readLine())!=null){
                if(tmp.equals(""));
                else
                    //将读到的readline()一行一行重新写入文件
                    writer.write(tmp+"\n");
            }
            writer.close();
            is.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}