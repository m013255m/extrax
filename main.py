package com.example.videouploader

import android.content.Context
import android.net.wifi.WifiManager
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.*
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.unit.dp
import com.example.videouploader.ui.theme.VideoUploaderTheme
import com.airbnb.lottie.compose.*
import android.os.VibrationEffect
import android.os.Vibrator
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Brightness4
import androidx.compose.material.icons.filled.Brightness7

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            var isDarkMode by remember { mutableStateOf(isSystemInDarkTheme()) }

            VideoUploaderTheme(darkTheme = isDarkMode) {
                DarkModeToggle(isDarkMode) {
                    isDarkMode = it
                }
                SplashScreen()
            }
        }
    }
}

@Composable
fun DarkModeToggle(isDarkMode: Boolean, onToggle: (Boolean) -> Unit) {
    IconButton(onClick = { onToggle(!isDarkMode) }) {
        if (isDarkMode) {
            Icon(Icons.Filled.Brightness7, contentDescription = "Switch to Light Mode")
        } else {
            Icon(Icons.Filled.Brightness4, contentDescription = "Switch to Dark Mode")
        }
    }
}

@Composable
fun SplashScreen() {
    var navigateToAPI by remember { mutableStateOf(false) }
    val composition by rememberLottieComposition(LottieCompositionSpec.Asset("splash_animation.json"))
    val progress by animateLottieCompositionAsState(
        composition = composition,
        iterations = LottieConstants.IterateForever
    )

    LaunchedEffect(key1 = progress) {
        if (progress == 1f) {
            navigateToAPI = true
        }
    }

    AnimatedVisibility(visible = !navigateToAPI) {
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            LottieAnimation(composition, progress, modifier = Modifier.size(300.dp))
            Text("Video Uploader", style = MaterialTheme.typography.h4)
        }
    }

    Crossfade(targetState = navigateToAPI) { screen ->
        if (screen) {
            APIScreen()
        }
    }
}

fun getMacAddress(context: Context): String? {
    val wifiManager = context.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager
    val wifiInfo = wifiManager.connectionInfo
    return wifiInfo.macAddress
}

@Composable
fun APIScreen() {
    var apiKey by remember { mutableStateOf(TextFieldValue("")) }
    var navigateToNext by remember { mutableStateOf(false) }
    val context = LocalContext.current

    AnimatedVisibility(visible = !navigateToNext) {
        Scaffold(
            topBar = { TopAppBar(title = { Text("Enter Activation Key") }) },
            content = {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    TextField(
                        value = apiKey,
                        onValueChange = { apiKey = it },
                        label = { Text("Activation Key") }
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = {
                        val vibrator = context.getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
                        vibrator.vibrate(VibrationEffect.createOneShot(100, VibrationEffect.DEFAULT_AMPLITUDE))

                        val macAddress = getMacAddress(context)
                        if (apiKey.text == macAddress) {  // تحقق من تطابق المفتاح مع الماك أدرس
                            navigateToNext = true
                        } else {
                            Snackbar {
                                Text("Invalid key for this device")
                            }
                        }
                    }) {
                        Text("Next")
                    }
                }
            }
        )
    }

    Crossfade(targetState = navigateToNext) { screen ->
        if (screen) {
            ContentSelectionScreen()
        }
    }
}

@Composable
fun ContentSelectionScreen() {
    var selectedContent by remember { mutableStateOf("") }
    var navigateToTimeScreen by remember { mutableStateOf(false) }

    AnimatedVisibility(visible = !navigateToTimeScreen) {
        Scaffold(
            topBar = { TopAppBar(title = { Text("Select Content") }) },
            content = {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text("Choose Video Topic")
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = {
                        selectedContent = "Horror Stories"
                        navigateToTimeScreen = true
                    }) {
                        Text("Horror Stories")
                    }
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = {
                        selectedContent = "Comedy Sketches"
                        navigateToTimeScreen = true
                    }) {
                        Text("Comedy Sketches")
                    }
                    // Add more content types here...
                }
            }
        )
    }

    Crossfade(targetState = navigateToTimeScreen) { screen ->
        if (screen) {
            ScheduleSelectionScreen()
        }
    }
}

@Composable
fun ScheduleSelectionScreen() {
    var timeToPublish by remember { mutableStateOf("21:00") }
    var navigateToDurationScreen by remember { mutableStateOf(false) }

    AnimatedVisibility(visible = !navigateToDurationScreen) {
        Scaffold(
            topBar = { TopAppBar(title = { Text("Select Time to Publish") }) },
            content = {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text("Choose Time for Video Publishing")
                    Spacer(modifier = Modifier.height(16.dp))
                    TextField(
                        value = timeToPublish,
                        onValueChange = { timeToPublish = it }
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = {
                        navigateToDurationScreen = true
                    }) {
                        Text("Next")
                    }
                }
            }
        )
    }

    Crossfade(targetState = navigateToDurationScreen) { screen ->
        if (screen) {
            VideoDurationScreen()
        }
    }
}

@Composable
fun VideoDurationScreen() {
    var duration by remember { mutableStateOf("10") }
    var isFinished by remember { mutableStateOf(false) }

    AnimatedVisibility(visible = !isFinished) {
        Scaffold(
            topBar = { TopAppBar(title = { Text("Select Video Duration") }) },
            content = {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text("Choose Video Duration (in minutes)")
                    Spacer(modifier = Modifier.height(16.dp))
                    TextField(
                        value = duration,
                        onValueChange = { duration = it }
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = {
                        isFinished = true
                    }) {
                        Icon(Icons.Default.Check, contentDescription = "Done")
                        Text("Finish")
                    }
                }
            }
        )
    }
}
