package com.example.harsh.cursorplot;

import android.annotation.SuppressLint;
import android.content.Context;
import android.graphics.Rect;
import android.os.Bundle;
import android.os.Vibrator;
import android.provider.Settings;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MotionEvent;
import android.widget.RelativeLayout;
import android.widget.Toast;

import com.example.harsh.cursorplot.API.APIClient;
import com.example.harsh.cursorplot.API.APIInterface;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    RelativeLayout dot1;
    RelativeLayout dot2;
    RelativeLayout dot3;
    RelativeLayout dot4;
    RelativeLayout dot5;
    RelativeLayout dot6;
    RelativeLayout dot7;
    RelativeLayout dot8;
    RelativeLayout dot9;
    StringBuffer speedBuffer, xyCoordinate, pressureValues;
    Long oldTimeStamp = -1L, diffTime = 0L, cumulativeDiff = 0L;
    Double xOld = -1.0, yOld = -1.0, diffX = 0.0, diffY = 0.0, speed = 0.0;
    APIInterface apiInterface;
    private Rect imageRect1;
    private Rect imageRect2;
    private Rect imageRect3;
    private Rect imageRect4;
    private Rect imageRect5;
    private Rect imageRect6;
    private Rect imageRect7;
    private Rect imageRect8;
    private Rect imageRect9;
    private String android_id;
    private Vibrator vb;

    @SuppressLint({"ClickableViewAccessibility", "HardwareIds"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.patternlock);

        this.dot1 = findViewById(R.id.dot1);
        this.dot2 = findViewById(R.id.dot2);
        this.dot3 = findViewById(R.id.dot3);
        this.dot4 = findViewById(R.id.dot4);
        this.dot5 = findViewById(R.id.dot5);
        this.dot6 = findViewById(R.id.dot6);
        this.dot7 = findViewById(R.id.dot7);
        this.dot8 = findViewById(R.id.dot8);
        this.dot9 = findViewById(R.id.dot9);

        vb = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
        apiInterface = APIClient.getClient().create(APIInterface.class);
        android_id = Settings.Secure.getString(getApplicationContext().getContentResolver(),
                Settings.Secure.ANDROID_ID);

        speedBuffer = new StringBuffer();
        xyCoordinate = new StringBuffer();
        pressureValues = new StringBuffer();
        speedBuffer.append("speed,time\n");
        xyCoordinate.append("x,y,time\n");
        pressureValues.append("pressure,time\n");
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        Log.e("onTouchEvent", "screen touched");
        if (this.imageRect1 == null) {
            this.imageRect1 = new Rect();
            this.dot1.getGlobalVisibleRect(this.imageRect1);
        }
        if (this.imageRect2 == null) {
            this.imageRect2 = new Rect();
            this.dot2.getGlobalVisibleRect(this.imageRect2);
        }
        if (this.imageRect3 == null) {
            this.imageRect3 = new Rect();
            this.dot3.getGlobalVisibleRect(this.imageRect3);
        }
        if (this.imageRect4 == null) {
            this.imageRect4 = new Rect();
            this.dot4.getGlobalVisibleRect(this.imageRect4);
        }
        if (this.imageRect5 == null) {
            this.imageRect5 = new Rect();
            this.dot5.getGlobalVisibleRect(this.imageRect5);
        }
        if (this.imageRect6 == null) {
            this.imageRect6 = new Rect();
            this.dot6.getGlobalVisibleRect(this.imageRect6);
        }
        if (this.imageRect7 == null) {
            this.imageRect7 = new Rect();
            this.dot7.getGlobalVisibleRect(this.imageRect7);
        }
        if (this.imageRect8 == null) {
            this.imageRect8 = new Rect();
            this.dot8.getGlobalVisibleRect(this.imageRect8);
        }
        if (this.imageRect9 == null) {
            this.imageRect9 = new Rect();
            this.dot9.getGlobalVisibleRect(this.imageRect9);
        }
        int x = (int) event.getX();
        int y = (int) event.getY();

        if (this.imageRect1.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect2.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect3.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect4.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect5.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect6.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect7.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect8.contains(x, y)) {
            vb.vibrate(10);
        }
        if (this.imageRect9.contains(x, y)) {
            vb.vibrate(10);
        }
        Double xCoordinate = (double) event.getX();
        Double yCoordinate = (double) event.getY();
        Long currentTimeStamp = System.currentTimeMillis();
        if (oldTimeStamp != -1) {
            diffTime = currentTimeStamp - oldTimeStamp;
        }
        if (xOld != -1) {
            diffX = Math.abs(xOld - xCoordinate);
        }
        if (yOld != -1) {
            diffY = Math.abs(yOld - yCoordinate);
        }
        if (diffTime != 0) {
            speed = Math.sqrt(diffX * diffX + diffY * diffY) / diffTime;
        } else {
            speed = 0.0;
        }
        cumulativeDiff += diffTime;
        oldTimeStamp = currentTimeStamp;
        xOld = xCoordinate;
        yOld = yCoordinate;

        speedBuffer.append(speed).append(",").append(cumulativeDiff).append("\n");
        pressureValues.append(event.getSize()).append(",").append(cumulativeDiff).append("\n");
        xyCoordinate.append(xCoordinate).append(",").append(yCoordinate).append(",").append(cumulativeDiff).append("\n");

        if (event.getAction() == MotionEvent.ACTION_UP) {
            Log.e("onTouchEvent", "finger action up");
            Map<String, Object> jsonParams = new HashMap<>();
            jsonParams.put("mode", "train");
            jsonParams.put("deviceId", android_id);
            jsonParams.put("xy", xyCoordinate.toString());
            jsonParams.put("speed", speedBuffer.toString());
            jsonParams.put("pressure", pressureValues.toString());
            RequestBody body = RequestBody.create(
                    okhttp3.MediaType.parse("application/json; charset=utf-8"),
                    (new JSONObject(jsonParams)).toString());
            apiInterface.uploadData(body).enqueue(new Callback<String>() {
                @Override
                public void onResponse(@NonNull Call<String> call, @NonNull Response<String> response) {
                    Toast.makeText(MainActivity.this, response.body(), Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onFailure(@NonNull Call<String> call, @NonNull Throwable t) {
                    Toast.makeText(MainActivity.this, t.getMessage(), Toast.LENGTH_SHORT).show();
                }
            });
            oldTimeStamp = -1L;
            diffTime = 0L;
            xOld = -1.0;
            yOld = -1.0;
            diffX = 0.0;
            diffY = 0.0;
            cumulativeDiff = 0L;
            speedBuffer = new StringBuffer();
            xyCoordinate = new StringBuffer();
            pressureValues = new StringBuffer();
            speedBuffer.append("speed,time\n");
            xyCoordinate.append("x,y,time\n");
            pressureValues.append("pressure,time\n");
        }
        return true;
    }
}
