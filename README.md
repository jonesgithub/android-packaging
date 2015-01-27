# Android-packaging
Android 打包工具

感谢 [美团打包]{http://tech.meituan.com/mt-apk-packaging.html}分享

使用方法：
- clone 到本地
- 编辑channels.txt文件,输入相关渠道

```cmd
  # python pack.py APK路径 输出目录  
  # 例如：
  python pack.py ./gengmei.apk gengmei
```
- Java代码中获取channel的方法
```java
public static String getChannel(Context context) {
		ApplicationInfo appinfo = context.getApplicationInfo();
		String sourceDir = appinfo.sourceDir;
		String ret = "";
		ZipFile zipfile = null;
		try {
			zipfile = new ZipFile(sourceDir);
			Enumeration<?> entries = zipfile.entries();
			while (entries.hasMoreElements()) {
				ZipEntry entry = ((ZipEntry) entries.nextElement());
				String entryName = entry.getName();
				//如果想修改此标示，直接编辑pack.py即可
				if (entryName.startsWith("META-INF/gmchannel")) {
					ret = entryName;
					break;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (zipfile != null) {
				try {
					zipfile.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		String[] split = ret.split("_");
		if (split != null && split.length >= 2) {
			return ret.substring(split[0].length() + 1);
		} else {
			return "";
		}
	}

```



