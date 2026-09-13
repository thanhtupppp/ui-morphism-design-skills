import 'dart:ui';
import 'package:flutter/material.dart';

class GlassSurface extends StatelessWidget {
  const GlassSurface({super.key});

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(20),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: const Color(0x24FFFFFF),
            border: Border.all(color: const Color(0x6BFFFFFF)),
            borderRadius: BorderRadius.circular(20),
          ),
          child: FilledButton(onPressed: () {}, child: const Text('Open panel')),
        ),
      ),
    );
  }
}
