package com.example.harsh.cursorplot.API;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface APIInterface {

    @POST("/upload")
    Call<String> uploadData(@Body RequestBody data);
//
//    @GET("/")
//    Call<String> uploadData1();
//
//    @GET("/hello")
//    Call<String> uploadData2();
}