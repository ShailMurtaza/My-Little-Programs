#include <stdio.h>
#include "lodepng.c"
#include <windows.h>

#define BOOL int
#define FAlSE 0
void SendScreenshot(char filename[]);
BOOL GetBMPScreen(HBITMAP bitmap, HDC bitmapDC, int width, int height, unsigned char** bufferOut, size_t* lengthOut)
{
	BOOL Success=FALSE;
	HDC SurfDC=NULL;
	HBITMAP OffscrBmp=NULL;
	HDC OffscrDC=NULL;
	LPBITMAPINFO lpbi=NULL;
	LPVOID lpvBits=NULL;
	HANDLE BmpFile=INVALID_HANDLE_VALUE;
	BITMAPFILEHEADER bmfh;

	if ((OffscrBmp = CreateCompatibleBitmap(bitmapDC, width, height)) == NULL)
		return FALSE;

	if ((OffscrDC = CreateCompatibleDC(bitmapDC)) == NULL)
		return FALSE;

	HBITMAP OldBmp = (HBITMAP)SelectObject(OffscrDC, OffscrBmp);
	BitBlt(OffscrDC, 0, 0, width, height, bitmapDC, 0, 0, SRCCOPY);
	lpbi = (LPBITMAPINFO)malloc(sizeof(BITMAPINFOHEADER) + 256 * sizeof(RGBQUAD));

	ZeroMemory(&lpbi->bmiHeader, sizeof(BITMAPINFOHEADER));
	lpbi->bmiHeader.biSize = sizeof(BITMAPINFOHEADER);

	SelectObject(OffscrDC, OldBmp);
	if (!GetDIBits(OffscrDC, OffscrBmp, 0, height, NULL, lpbi, DIB_RGB_COLORS))
		return FALSE;

	lpvBits = malloc(lpbi->bmiHeader.biSizeImage);

	if (!GetDIBits(OffscrDC, OffscrBmp, 0, height, lpvBits, lpbi, DIB_RGB_COLORS))
		return FALSE;

	int h = height;
	int w = width;
	unsigned scanlineBytes = w * 4;
	if(scanlineBytes % 4 != 0) scanlineBytes = (scanlineBytes / 4) * 4 + 4;

	char *png = malloc(w * h * 4);
	int x,y;
	for(y = 0; y < h; y++)
		for(x = 0; x < w; x++)
		{
			unsigned bmpos = (h - y - 1) * scanlineBytes + 4 * x;
			unsigned newpos = 4 * y * w + 4 * x;

			png[newpos + 0] = ((char *)lpvBits)[bmpos + 2]; //R
			png[newpos + 1] = ((char *)lpvBits)[bmpos + 1]; //G
			png[newpos + 2] = ((char *)lpvBits)[bmpos + 0]; //B
			png[newpos + 3] = 255;            //A
	}


	free(lpvBits);
	lodepng_encode32_memory(png, width, height, bufferOut, lengthOut);
	free(png);

	return TRUE;
}


void SendScreenshot(char filename[])
{
	HDC hDc = CreateCompatibleDC(0);
	int width = GetDeviceCaps(hDc, HORZRES);
	int height = GetDeviceCaps(hDc, VERTRES);
	HBITMAP hBmp = CreateCompatibleBitmap(GetDC(0), width, height);
	SelectObject(hDc, hBmp);
	BitBlt(hDc, 0, 0, width, height, GetDC(0), 0, 0, SRCCOPY);

	unsigned char *image;
	size_t len;

	BOOL ret = GetBMPScreen(hBmp, hDc, width, height, &image, &len);

	DeleteObject(hBmp);
	DeleteObject(hDc);

	FILE * img = fopen(filename, "wb");
	fwrite(image, 1, len, img);
	fclose(img);

	lodepng_memory_free(image);
}

int main()
{
	int i;
	char filename[10];
	for(i=0;i<10;i++)
	{
		sprintf(filename, "test%d.png", i);
		SendScreenshot(filename);
	}
	return 0;
}

