import 'package:flutter/material.dart';

class AuroraBackground extends StatelessWidget {
  const AuroraBackground({super.key});

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: const BoxDecoration(
        gradient: RadialGradient(
          center: Alignment(-0.7, -0.8),
          radius: 1.4,
          colors: [Color(0xFF6D5DFC), Color(0xFF0D1021)],
          stops: [0.0, 1.0],
        ),
      ),
      child: Center(
        child: Card(
          elevation: 0,
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: FilledButton(onPressed: () {}, child: const Text('Explore')),
          ),
        ),
      ),
    );
  }
}
